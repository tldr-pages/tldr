import os
from enum import Enum

import requests
from bs4 import BeautifulSoup

class DisplayType(Enum):
	"""
	An enum which specifies how the content is displayed in the wiki page.
	In some pages, we have to parse a list in a table row.
	In some, we have to parse from a column in a table.
	"""
	LIST = 1
	TABLE = 2

class Extractor(object):
	"""
	This extracts the commands from both the local filesystem and wikipedia
	"""
	def __init__(self):
		self.linux_pages = [
			{'url': 'https://en.wikipedia.org/wiki/Template:Unix_commands', 'display_type': DisplayType.LIST},
			{'url': 'https://en.wikipedia.org/wiki/List_of_Unix_commands', 'display_type': DisplayType.TABLE},
			{'url': 'https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands', 'display_type': DisplayType.TABLE}
		]

		self.page_root = 'pages'
		self.common_folder = os.path.join(self.page_root, 'common')
		self.linux_folder = os.path.join(self.page_root, 'linux')
		self.windows_folder = os.path.join(self.page_root, 'windows')
		self.macos_folder = os.path.join(self.page_root, 'osx')

	def get_linux_commands(self):
		"""
		Returns linux commands from local and wikipedia
		"""
		linux_commands = self.get_local_commands()
		wiki_commands = self.parse_wiki_pages()
		return linux_commands, wiki_commands

	def get_local_commands(self):
		"""
		Gets the list of commands for the linux folder.
		It always merges the commands from common and then strips the file extension
		"""
		common_files = [item for item in os.listdir(self.common_folder) if item.endswith('.md')]
		platform_files = [item for item in os.listdir(self.linux_folder) if item.endswith('.md')]
		commands = list(set(common_files + platform_files))
		commands = [os.path.splitext(item)[0] for item in commands]
		return commands

	def parse_wiki_pages(self):
		"""
		Parses the wiki pages and extracts the commands from there
		"""
		all_commands = []

		for page in self.linux_pages:
			r = requests.get(page["url"])
			print('getting commands from- ', page["url"])
			if page["display_type"] == DisplayType.LIST:
				all_commands += self.handle_list_type_page(r.text.replace('\n',''))

			if page["display_type"] == DisplayType.TABLE:
				all_commands += self.handle_table_type_page(r.text.replace('\n',''))

		# deduplicating the commands
		all_commands = list(set(all_commands))
		return all_commands

	def handle_list_type_page(self, html):
		"""
		This extracts commands from a wiki page which has entries in a list form
		"""
		parsed_html = BeautifulSoup(html, 'html.parser')
		table = parsed_html.find('div', id='mw-content-text').find('table')
		commands = []
		for row in table.find_all('tr'):
			# filter rows with only 2 columns.
			# Sometimes, we get headers and footers with no info. So need to ignore those
			if len(row.contents) < 2:
				continue
			# get the <li>s and extract the text node from <a>
			for li in row.contents[1].find_all('li'):
				commands.append(li.find('a').text.strip().lower())
		return commands

	def handle_table_type_page(self, html):
		"""
		This extracts commands from a wiki page which has entries in a table form
		"""
		parsed_html = BeautifulSoup(html, 'html.parser')
		table = parsed_html.find('div', id='mw-content-text').find('table', class_='wikitable sortable')

		commands = []
		for row in table.find_all('tr'):
			elems = row.find_all('td')
			# ignoring rows with no td
			if len(elems) == 0:
				continue
			# ignoring obsolete commands
			if elems[2].text.strip().startswith('Obscalescent'):
				continue
			# if link present
			if elems[0].find('a'):
				commands.append(elems[0].find('a').text.strip().lower())
			else: # else get the node content
				commands.append(elems[0].text.strip().lower())
		return commands

