# ag

> The Silver Searcher. Like ack, but faster.

- Find files containing "foo", and print the line matches in context (`-F` is an alias for `--literal`):

`ag -F {{foo}}`

- Find files containing "foo", but only list the filenames:

`ag -F -l {{foo}}`

- Find files containing "FOO" case-insensitively, and print only the match, rather than the whole line:

`ag -F -i -o {{FOO}}`

- Find "foo" in files with a name matching the regex "bar":

`ag -F {{foo}} -G {{bar}}`

- Find files whose contents match a regular expression:

`ag '{{^ba(r|z)$}}'`

- Find files with a name matching the regex "foo":

`ag -g {{foo}}`
