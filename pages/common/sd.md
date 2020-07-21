# sd

> Intuitive find & replace CLI.

- Trim some whitespace using regex:

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- Replace words using capture groups:

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Find and replace in a file printing the result to stdout:

`sd -p {{'window.fetch'}} {{'fetch'}} {{http.js}}`

- Find and replace across a project changing each file in place:

`sd {{'from "react"'}} {{'from "preact"'}} $(find . -type f)`
