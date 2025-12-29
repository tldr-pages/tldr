# go test

> Testa i pacchetti Go (i file devono terminare con `_test.go`).
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

- Testa il pacchetto trovato nella directory corrente:

`go test`

- Testa verbose il pacchetto nella directory corrente:

`go test -v`

- Testa i pacchetti nella directory corrente e tutte le sottodirectory (nota i `...`):

`go test -v ./...`

- Testa il pacchetto nella directory corrente ed esegue tutti i benchmark:

`go test -v -bench .`

- Testa il pacchetto nella directory corrente ed esegue tutti i benchmark per 50 secondi:

`go test -v -bench . -benchtime 50s`

- Testa il pacchetto con analisi di copertura:

`go test -cover`
