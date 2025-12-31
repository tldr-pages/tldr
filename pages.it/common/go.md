# go

> Gestisci il codice sorgente Go.
> Alcuni sottocomandi come `build` hanno la propria documentazione d'uso.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go>.

- Scarica e installa un pacchetto, specificato tramite il suo import path:

`go get {{percorso/del/pacchetto}}`

- Compila ed esegui un file sorgente (deve contenere un package `main`):

`go run {{percorso/del/file}}.go`

- Compila un file sorgente in un eseguibile con nome specifico:

`go build -o {{eseguibile}} {{percorso/del/file}}.go`

- Compila il pacchetto presente nella directory corrente:

`go build`

- Esegui tutti i test del pacchetto corrente (i file devono terminare con `_test.go`):

`go test`

- Compila e installa il pacchetto corrente:

`go install`

- Inizializza un nuovo modulo nella directory corrente:

`go mod init {{nome_modulo}}`
