# go clean

> Rimuove file oggetto e file cached.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Remove_object_files_and_cached_files>.

- Stampa i comandi di rimozione invece di rimuovere effettivamente:

`go clean -n`

- Elimina la cache di build:

`go clean -cache`

- Elimina tutti i risultati dei test cached:

`go clean -testcache`

- Elimina la cache dei moduli:

`go clean -modcache`
