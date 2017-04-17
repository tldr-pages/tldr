#!/bin/bash

#set -x	# debug

verbose=1
url="http://man7.org/linux/man-pages/man1/"
ext=.1.html

url="${url%/}/"	# add trailng slash if missing
ext=".${ext#.}"	# add leading dot if missing

check() {
	test "`curl -s -o /dev/null -I -w "%{http_code}" "$url$1$ext"`" = "200"
}

# main code
for fn in *
do
	c=${fn%.md}
	if check "$c"
	then
		(($verbose)) && echo $c
		perl -pi~ -e "1...1 and s<^(# )$c\s*\$><\${1}[$c]($url$c$ext)>" "$fn" \
			|| echo 1>&2 "Error updating ‘$fn’."
	else
		echo 1>&2 "There is no man page for ‘$c’ at ‘$url’."
	fi
done

#rm *~	# delete backup files

# vi: set ts=2 sw=2 nowrap:
