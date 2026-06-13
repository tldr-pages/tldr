# go doc

> Visualizza la documentazione per un pacchetto o simbolo.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Show_documentation_for_package_or_symbol>.

- Visualizza la documentazione del pacchetto corrente:

`go doc`

- Mostra la documentazione del pacchetto e i simboli esportati:

`go doc {{encoding/json}}`

- Mostra anche la documentazione di tutti i simboli:

`go doc -all {{encoding/json}}`

- Mostra anche il sorgente:

`go doc -all -src {{encoding/json}}`

- Mostra un simbolo specifico:

`go doc -all -src {{encoding/json.Number}}`
