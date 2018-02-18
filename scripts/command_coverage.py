#!/usr/bin/env python3
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

# Constants
LINUX_PAGES = [
	{'url': 'https://en.wikipedia.org/wiki/Template:Unix_commands', 'display_type': DisplayType.LIST},
	{'url': 'https://en.wikipedia.org/wiki/List_of_Unix_commands', 'display_type': DisplayType.TABLE},
	{'url': 'https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands', 'display_type': DisplayType.TABLE}
]

PAGE_ROOT = 'pages'
COMMON_FOLDER = os.path.join(PAGE_ROOT, 'common')
LINUX_FOLDER = os.path.join(PAGE_ROOT, 'linux')
WINDOWS_FOLDER = os.path.join(PAGE_ROOT, 'windows')
MACOS_FOLDER = os.path.join(PAGE_ROOT, 'osx')

def get_commands(folder_path):
	"""
	Gets the list of commands for a given platform folder.
	It always merges the commands from common and then strips the file extension
	"""
	common_files = [item for item in os.listdir(COMMON_FOLDER) if item.endswith('.md')]
	platform_files = [item for item in os.listdir(folder_path) if item.endswith('.md')]
	commands = list(set(common_files + platform_files))
	commands = [os.path.splitext(item)[0] for item in commands]
	return commands

def parse_wiki_page():
	"""
	Parses the wiki pages and extracts the commands from there
	"""
	all_commands = []

	for page in LINUX_PAGES:
		r = requests.get(page["url"])
		if page["display_type"] == DisplayType.LIST:
			parsed_html = BeautifulSoup(r.text.replace('\n',''), 'html.parser')
			table = parsed_html.find('div', id='mw-content-text').find('table')

			print('printing commands from- ', page["url"])
			for row in table.find_all('tr'):
				# filter rows with only 2 columns.
				# Sometimes, we get headers and footers with no info. So need to ignore those
				if len(row.contents) < 2:
					continue
				# get the <li>s and extract the text node from <a>
				for li in row.contents[1].find_all('li'):
					all_commands.append(li.find('a').text.strip().lower())

		if page["display_type"] == DisplayType.TABLE:
			parsed_html = BeautifulSoup(r.text.replace('\n',''), 'html.parser')
			table = parsed_html.find('div', id='mw-content-text').find('table', class_='wikitable sortable')

			print('printing commands from- ', page["url"])
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
					all_commands.append(elems[0].find('a').text.strip().lower())
				else: # else get the node content
					all_commands.append(elems[0].text.strip().lower())

	all_commands = list(set(all_commands))
	return all_commands

if __name__ == '__main__':
	# execute only for master
	#if os.environ.get('TRAVIS_BRANCH') != "master":
	#	return

	# get existing linux pages
	linux_commands = get_commands(LINUX_FOLDER)
	# print(linux_commands)

	# get list of all pages
	wiki_commands = parse_wiki_page()

	# compare
	diff = len(set(wiki_commands) - set(linux_commands))
	print('percent covg- ', (diff/len(wiki_commands))*100)

	# get number from svg badge

	# update file only if there is a change
