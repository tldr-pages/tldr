# ag

> The Silver Searcher. Like `ack`, but aims to be faster.
> More information: <https://github.com/ggreer/the_silver_searcher>.

- Find files containing "foo", and print the line matches in context:

`ag {{foo}}`

- Find files containing "foo" in a specific directory:

`ag {{foo}} {{path/to/directory}}`

- Find files containing "foo", but only [l]ist the filenames:

`ag -l {{foo}}`

- Find files containing "FOO" case-[i]nsensitively, and print [o]nly the match, rather than the whole line:

`ag -i -o {{FOO}}`

- Find "foo" in files with a name matching "bar":

`ag {{foo}} -G {{bar}}`

- Find files whose contents match a regular expression:

`ag '{{^ba(r|z)$}}'`

- Find files with a name matching "foo":

`ag -g {{foo}}`
