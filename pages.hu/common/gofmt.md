# gofmt

> Go forráskód formázására szolgáló eszköz. További információ: <https://golang.org/cmd/gofmt/>.

- Egy fájl formázása és az eredmény megjelenítése a konzolon:

`gofmt {{source.go}}`

- Egy fájl formázása, az eredeti fájl helyben történő felülírásával:

`gofmt -w {{source.go}}`

- Formázzon meg egy fájlt, majd egyszerűsítse a kódot, felülírva az eredeti fájlt:

`gofmt -s -w {{source.go}}`

- Az összes (beleértve a téves) hiba kiírása:

`gofmt -e {{source.go}}`
