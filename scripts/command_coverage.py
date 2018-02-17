#!/usr/bin/env python3
import os

LINUX_PAGES = [
	'https://en.wikipedia.org/wiki/Template:Unix_commands',
	'https://en.wikipedia.org/wiki/List_of_Unix_commands',
	'https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands'
]

PAGE_ROOT = 'pages'
COMMON_FOLDER = os.path.join(PAGE_ROOT, 'common')
LINUX_FOLDER = os.path.join(PAGE_ROOT, 'linux')
WINDOWS_FOLDER = os.path.join(PAGE_ROOT, 'windows')
MACOS_FOLDER = os.path.join(PAGE_ROOT, 'osx')

def get_commands(folder_path):
	common_files = [item for item in os.listdir(COMMON_FOLDER) if item.endswith('.md')]
	platform_files = [item for item in os.listdir(folder_path) if item.endswith('.md')]
	# getting the unique list
	commands = list(set(common_files + platform_files))
	# removing .md extension
	commands = [os.path.splitext(item)[0] for item in commands]
	return commands

if __name__ == '__main__':
	# execute only for master
	#if os.environ.get('TRAVIS_BRANCH') != "master":
	#	return
	# get existing linux pages
	linux_commands = get_commands(LINUX_FOLDER)
	print(linux_commands)

	# get list of all pages

	# compare

	# get number from svg badge

	# update file only if there is a change
	print('hello')
