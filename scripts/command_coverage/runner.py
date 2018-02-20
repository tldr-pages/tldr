#!/usr/bin/env python3
import os
from xml.dom import minidom

import extractor
from uploader import upload_file

SVG_FILE = 'command_coverage.svg'

if __name__ == '__main__':
	# execute only for master
	#if os.environ.get('TRAVIS_BRANCH') != "master":
	#	return

	# do not execute for the commits to update command coverage
	commit_msg = os.environ.get('TRAVIS_COMMIT_MESSAGE')
	if commit_msg and commit_msg.startswith('[command coverage]'):
		os.exit(0)

	# initialize extractor and get the commands
	extractor = extractor.Extractor()
	linux_commands, wiki_commands = extractor.get_linux_commands()

	# compare
	diff = len(set(wiki_commands) - set(linux_commands))
	print('current count- ', len(set(linux_commands)))
	print('total count- ', len(set(wiki_commands)))
	current_percent = int((diff/len(wiki_commands))*100)

	# get number from svg badge
	svg_dom = minidom.parse(SVG_FILE)
	tags = svg_dom.getElementsByTagName('text')
	existing_percent = int(tags[2].firstChild.nodeValue)

	# update file only if there is a change
	if current_percent != existing_percent:
		print('updating the file')
		tags[2].firstChild.nodeValue = current_percent
		tags[3].firstChild.nodeValue = current_percent

		# push the new file to git
		upload_file(svg_dom, SVG_FILE)

