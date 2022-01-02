# rnm

> Batch renaming tool.

> More information: <https://github.com/neurobin/rnm>.

- Rename a file adding a specific text to the filename:

`rnm -ns '/fn/ some text to add' oldfile`

- Rename all files in the current directory appending an index to the filename:

`rnm -ns '/n/ /i/./e/' ./*`

- Append index with leading zeroes and with starting index 4:

`rnm -ns '/n/ /id/./e/' -ifl 3 -inc 1 -si 4 ./*`

- Rename all files in the current directory replacing underscores with spaces ('/regex/replace/modifier'):

`rnm -rs '/_/ /g' ./*`
