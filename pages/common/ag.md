# ag

> The Silver Searcher. Like `ack`, but aims to be faster.
> More information: <https://manned.org/ag>.

- Find files containing `string`, and print the line matches in context:

`ag string`

- Find files containing `string` in a specific directory:

`ag string {{path/to/directory}}`

- Find files containing `string`, but only list the filenames:

`ag {{[-l|--files-with-matches]}} string`

- Find files containing `STRING` case-insensitively, and print only the match, rather than the whole line:

`ag {{[-i|--ignore-case]}} {{[-o|--only-matching]}} STRING`

- Find `string` in files with a name matching `file_name`:

`ag string {{[-G|--file-search-regex]}} file_name`

- Find files whose contents match a `regex`:

`ag '{{^ca(t|r)$}}'`

- Find files with a name matching `string`:

`ag {{[-g|--filename-pattern]}} string`
