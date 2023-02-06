# go fmt

> Go forrásfájlok formázása. A megváltoztatott fájlnevek nyomtatása. További információ: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- Az aktuális könyvtárban lévő Go forrásfájlok formázása:

`go fmt`

- Az importálási útvonalban lévő konkrét Go csomag formázása (`$GOPATH/src`):

`go fmt {{path/to/package}}`

- Az aktuális könyvtárban és az összes alkönyvtárban lévő csomag formázása (vegye figyelembe a `...`):

`go fmt {{./...}}`

- Kiírja, hogy milyen formázási parancsokat futtatott volna, anélkül, hogy bármit is módosítana:

`go fmt -n`

- Nyomtassa ki, hogy mely formázási parancsok futnak, ahogyan azok futnak:

`go fmt -x`
