# go build

> Compila pacchetti e dipendenze.
> Maggiori informazioni: <https://pkg.go.dev/cmd/go#hdr-Compile_packages_and_dependencies>.

- Compila un file 'package main' (l'output sarà il nome del file senza estensione):

`go build {{percorso/del/main.go}}`

- Compila, specificando il nome del file di output:

`go build -o {{percorso/del/binary}} {{percorso/del/source.go}}`

- Compila un pacchetto:

`go build -o {{percorso/del/binary}} {{percorso/del/package}}`

- Compila un pacchetto main in un eseguibile, abilitando il rilevamento race condition:

`go build -race -o {{percorso/dell/eseguibile}} {{percorso/del/pacchetto_main}}`
