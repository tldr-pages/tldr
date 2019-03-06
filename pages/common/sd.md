# sd

> `sd` is an intuitive find & replace CLI.

- Trim some whitespace using regex:

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- Replace words using capture groups:

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Find and replace in a file:

`sd -i {{'window.fetch'}} {{'fetch'}} {{http.js}}`

- Find and replace across a project:

`sd -i {{'from "react"'}} {{'from "preact"'}} $(find . -type f)`
