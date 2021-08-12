# go

> Instrument pentru gestionarea codului sursă go.
> Mai multe informaţii: <https://golang.org>

- Descărcați și instalați un pachet, specificat de calea sa de import:

`go get {{package_path}}`

- Compilarea și rularea unui fișier sursă (trebuie să conțină un pachet „principal”):

`go run {{file}}.go`

- Compilarea unui fișier sursă într-un executabil denumit:

`go build -o {{executable}} {{file}}.go`

- Compilați pachetul prezent în directorul curent:

`go build`

- Executa toate cazurile de testare ale pachetului curent (fisierele trebuie sa se incheie cu `_test.go`):

`go test`

- Compilați și instalați pachetul curent:

`go install`

- Inițializarea unui nou modul în directorul curent:

`go mod init {{module_name}}`
