# gofmt

> Instrument pentru formatare Go cod sursă.
> Mai multe informaţii: <https://golang.org/cmd/gofmt/>

- Formatați un fișier și afișați rezultatul la consola:

`gofmt {{source.go}}`

- Formatarea unui fișier, suprascrierea fișierului original în loc:

`gofmt -w {{source.go}}`

- Formatați un fișier, și apoi simplificați codul, suprascrierea fișierul original:

`gofmt -s -w {{source.go}}`

- Imprimați toate erorile (inclusiv false):

`gofmt -e {{source.go}}`
