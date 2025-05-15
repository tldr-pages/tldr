# ag

> The Silver Searcher. Like `ack`, but aims to be faster.
> More information: <https://manned.org/ag>.

- Find files containing "foo", and print the line matches in context:

`ag foo`

- Find files containing "foo" in a specific directory:

`ag foo {{path/to/directory}}`

- Find files containing "foo", but only list the filenames:

`ag {{[-l|--files-with-matches]}} foo`

- Find files containing "FOO" case-insensitively, and print only the match, rather than the whole line:

`ag {{[-i|--ignore-case]}} {{[-o|--only-matching]}} FOO`

- Find "foo" in files with a name matching "bar":

`ag foo {{[-G|--file-search-regex]}} bar`

- Find files whose contents match a regular expression:

`ag '{{^ba(r|z)$}}'`

- Find files with a name matching "foo":

`ag {{[-g|--filename-pattern]}} foo`
