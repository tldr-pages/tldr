# sd

> Intuitív keresés és csere CLI. További információ: <https://github.com/chmln/sd>.

- Néhány szóköz levágása szabályos kifejezéssel (kimeneti folyam: `stdout`):

`{{echo 'lorem ipsum 23 '}} | sd '\s+$' ''`

- Szavak cseréje rögzítési csoportok használatával (kimeneti folyam: `stdout`):

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Keresés és csere egy adott fájlban (kimeneti folyam: `stdout`):

`sd -p {{'window.fetch'}} {{'fetch'}} {{path/to/file.js}}`

- Keresés és csere az aktuális projekt összes fájljában (kimeneti folyam: `stdout`):

`sd {{'from "react"'}} {{'from "preact"'}} "$(find . -type f)"`
