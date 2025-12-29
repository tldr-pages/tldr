# go install

> Compila e installa i pacchetti nominati dai percorsi di import.
> Ulteriori informazioni: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- Compila e installa il pacchetto corrente:

`go install`

- Compila e installa un pacchetto locale specifico:

`go install {{percorso/del/pacchetto}}`

- Installa l'ultima versione di un programma, ignorando `go.mod` nella directory corrente:

`go install {{golang.org/x/tools/gopls}}@{{latest}}`

- Installa un programma alla versione selezionata da `go.mod` nella directory corrente:

`go install {{golang.org/x/tools/gopls}}`
