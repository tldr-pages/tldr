# sd

> Intuitive find and replace.
> More information: <https://github.com/chmln/sd>.

- Trim some whitespace using a regular expression (output stream: `stdout`):

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- Replace words using capture groups (output stream: `stdout`):

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Find and replace in a specific file (output stream: `stdout`):

`sd -p {{'window.fetch'}} {{'fetch'}} {{path/to/file.js}}`

- Find and replace in all files in the current project (output stream: `stdout`):

`sd {{'from "react"'}} {{'from "preact"'}} "$(find . -type f)"`
