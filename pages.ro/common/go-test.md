# go test

> Teste Go pachete (fișierele trebuie să se încheie cu `_test.go`).
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-Testing_flags>

- Testați pachetul găsit în directorul curent:

`go test`

- [v] testați erbosely pachetul în directorul curent:

`go test -v`

- Testați pachetele din directorul curent și din toate subdirectoarele (notați „...”):

`go test -v ./...`

- Testați pachetul în directorul curent și executați toate valorile de referință:

`go test -v -bench .`

- Testați pachetul în directorul curent și executați toate valorile de referință timp de 50 de secunde:

`go test -v -bench . -benchtime {{50s}}`
