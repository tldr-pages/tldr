#!/bin/bash
# This script performs the following:
# - Generate configuration file for po4a (can be configured in CONFIGFILE)
# - Generate POT file from pages/<DIRECTORY>/*.md
# - Update PO files in i18n directory with POT file
# - Generate localized pages.XX/<DIRECTORY>/*.md (where XX is the language code)
# - Remove unneeded new lines from generated pages

# Name of the po4a configuration file
CONFIGFILE='po4a.conf'

# List of supported languages
LANGS=(hu)

# Generate po4a.conf file with list of TLDR pages
echo 'Generating configuration file for po4a...'

echo '# WARNING: this file is generated with translation-update.sh' > $CONFIGFILE
echo '# DO NOT modify this file manually!' >> $CONFIGFILE
echo -e >> $CONFIGFILE
echo "[po4a_langs] ${LANGS[*]}" >> $CONFIGFILE
echo '[po4a_paths] i18n/tldr.pot $lang:i18n/tldr.$lang.po' >> $CONFIGFILE
echo -e >> $CONFIGFILE
for FILE in `tree -f -i pages | grep ".md"`
do
	echo [type: asciidoc] $FILE \$lang:pages.\$lang/`echo $FILE | cut -d"/" -f 2`/`echo $FILE | cut -d"/" -f 3` >> $CONFIGFILE
done

# Generate POT file, PO files, and pages.XX pages
echo 'Generating POT file and translated TLDR pages...'
po4a -k 0 --msgid-bugs-address 'https://github.com/tldr-pages/tldr/issues' $CONFIGFILE

# Beautify translated TLDR pages (remove unneeded new lines)
for LANG in "${LANGS[@]}"
do
	echo "Beautifying TLDR pages ($LANG)..."
	for FILE in `tree -f -i pages.$LANG | grep ".md"`
	do
		# Remove unneeded new lines
		sed -i '/^[#|>|-].*$/{$!N; s/\n  / /g;ty;P;D;:y}' $FILE

		# Run again for 3-lines strings, as the first run only removes the first new line
		sed -i '/^[#|>|-].*$/{$!N; s/\n  / /g;ty;P;D;:y}' $FILE

		# Remove unneeded new lines from commands (lines like `...`)
		sed -i '/^`.*$/{$!N; s/\n\(.\{1,\}\)/ \1/g;ty;P;D;:y}' $FILE

		# Run again for 3-lines commands, as the first run only removes the first new line
		sed -i '/^`.*$/{$!N; s/\n\(.\{1,\}\)/ \1/g;ty;P;D;:y}' $FILE
	done
done
