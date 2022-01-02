# rnm

> Batch renaming tool.

> More information: https://github.com/neurobin/rnm

- Rename by adding something to oldname:

`rnm -ns '/fn/ some text to add' oldfile`

- Rename all by appending index to file names:

`rnm -ns '/n/ /i/./e/' ./*`

- Append index with leading zeroes and with starting index 4:

`rnm -ns '/n/ /id/./e/' -ifl 3 -inc 1 -si 4 ./*`

- Change underscores to spaces in file name ('/regex/replace/modifier'):

`rnm -rs '/_/ /g' ./*`
