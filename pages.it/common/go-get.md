# go get

> Aggiunge un pacchetto di dipendenza o scarica pacchetti in modalità GOPATH legacy.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- Aggiunge il pacchetto specificato a `go.mod` in modalità modulo o installa il pacchetto in modalità GOPATH:

`go get {{example.com/pkg}}`

- Modifica il pacchetto con una versione specifica in modalità module-aware:

`go get {{example.com/pkg}}@{{v1.2.3}}`

- Rimuove un pacchetto specificato:

`go get {{example.com/pkg}}@{{none}}`
