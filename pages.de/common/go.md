# go

> Verwalte Go-Quellcode.
> Einige Unterbefehle wie `build` haben ihre eigene Nutzungsdokumentation.
> Weitere Informationen: <https://pkg.go.dev/cmd/go>.

- Lade ein Paket herunter und installiere es, angegeben durch seinen Import-Pfad:

`go get {{pfad/zu/paket}}`

- Kompiliere und führe eine Quelldatei aus (sie muss ein `main`-Paket enthalten):

`go run {{datei}}.go`

- Kompiliere eine Quelldatei in eine benannte ausführbare Datei:

`go build -o {{ausführbare_datei}} {{datei}}.go`

- Kompiliere das Paket, das im aktuellen Verzeichnis vorhanden ist:

`go build`

- Führe alle Testfälle des aktuellen Pakets aus (Dateien müssen mit `_test.go` enden):

`go test`

- Kompiliere und installiere das aktuelle Paket:

`go install`

- Initialisiere ein neues Modul im aktuellen Verzeichnis:

`go mod init {{modul_name}}`
