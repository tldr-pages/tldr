# sd

> Găsiți intuitiv și înlocuiți CLI.

- Îndepărtați un spațiu alb folosind o expresie regulată:

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- Înlocuiți cuvintele folosind grupuri de captare:

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Găsiți și înlocuiți într-un fișier care imprimă rezultatul la stdout:

`sd -p {{'window.fetch'}} {{'fetch'}} {{http.js}}`

- Găsiți și înlocuiți într-un proiect care schimbă fiecare fișier în loc:

`sd {{'from "react"'}} {{'from "preact"'}} $(find . -type f)`
