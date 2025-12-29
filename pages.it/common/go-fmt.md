# go fmt

> Formatta i sorgenti Go, stampando i nomi dei file modificati.
> Ulteriori informazioni: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- Formatta i sorgenti Go nella directory corrente:

`go fmt`

- Formatta un pacchetto Go specifico nel percorso di import (`$GOPATH/src`):

`go fmt {{percorso/del/pacchetto}}`

- Formatta il pacchetto nella directory corrente e tutte le sottodirectory (nota i `...`):

`go fmt {{./...}}`

- Stampa i comandi di formattazione che sarebbero eseguiti, senza modificare nulla:

`go fmt -n`

- Stampa i comandi di formattazione mentre vengono eseguiti:

`go fmt -x`
