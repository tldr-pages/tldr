# ag

> The Silver Searcher. Like ack, but faster.

- Find files containing "foo"

`ag foo`

- Find "foo" in files with a name matching "bar"

`ag foo -G bar`

- Find files whose contents match a regular expression:

`ag '^ba(r|z)$'`

- Find files whose contents match a literal expression, not a regular expression:

`ag -Q '.bar'`

- Find files with a name matching "foo"

`ag -g foo`
