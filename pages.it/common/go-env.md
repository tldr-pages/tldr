# go env

> Gestisci le variabili d'ambiente usate dal toolchain Go.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Print_Go_environment_information>.

- Mostra tutte le variabili d'ambiente:

`go env`

- Mostra una variabile d'ambiente specifica:

`go env {{GOPATH}}`

- Imposta una variabile d'ambiente a un valore:

`go env -w {{GOBIN}}={{percorso/della/directory}}`

- Resetta il valore di una variabile d'ambiente:

`go env -u {{GOBIN}}`
