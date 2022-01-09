# rnm

> Batch renaming tool.
> More information: <https://github.com/neurobin/rnm>.

- Rename a file adding a specific text to the filename:

`rnm -ns '/fn/{{text_to_add}}' {{path/to/file}}`

- Rename all files in the current directory appending an index to the filename:

`rnm -ns '{{/n/ /i/./e/}}' {{./*}}`

- Append an index with leading zeroes, starting at an index of 4:

`rnm -ns '/n/ /id/./e/' -ifl 3 -inc 1 -si 4 ./*`

- Rename all files in the current directory replacing underscores with spaces ('/regex/replace/modifier'):

`rnm -rs '{{/_/ /g}}' {{./*}}`
