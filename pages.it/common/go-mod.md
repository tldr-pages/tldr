# go mod

> Manutenzione moduli.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Module_maintenance>.

- Inizializza nuovo modulo nella directory corrente:

`go mod init {{nomeModulo}}`

- Scarica moduli nella cache locale:

`go mod download`

- Aggiungi moduli mancanti e rimuovi quelli inutilizzati:

`go mod tidy`

- Verifica che le dipendenze abbiano il contenuto atteso:

`go mod verify`

- Copia le sorgenti di tutte le dipendenze nella directory vendor:

`go mod vendor`
