# ag

> The Silver Searcher. Like ack, but faster.

- Find files containing "foo":

`ag foo`

- Find files containing "FOO" case-insensitively:

`ag -i FOO`

- Find "foo" in files with a name matching "bar":

`ag foo -G bar`

- Find files whose contents match a regular expression:

`ag '^ba(r|z)$'`

- Find files with a name matching "foo":

`ag -g foo`
