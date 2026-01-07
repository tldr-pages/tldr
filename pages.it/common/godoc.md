# godoc

> Visualizza la documentazione per i pacchetti Go.
> Maggiori informazioni: <https://pkg.go.dev/golang.org/x/tools/cmd/godoc>.

- Mostra l'aiuto per un pacchetto specifico:

`godoc {{fmt}}`

- Mostra l'aiuto per la funzione "Printf" del pacchetto "fmt":

`godoc {{fmt}} {{Printf}}`

- Serve la documentazione come web server sulla porta 6060:

`godoc -http=:{{6060}}`

- Crea un file indice:

`godoc -write_index -index_files={{percorso/del/file}}`

- Usa il file indice specificato per cercare nella documentazione:

`godoc -http=:{{6060}} -index -index_files={{percorso/del/file}}`
