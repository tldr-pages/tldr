# go test

> Go csomagok tesztelése (a fájloknak a `_test.go` végződéssel kell végződniük). További információ: [https://golang.org/cmd/go/#hdr-Testing_flags.](https://golang.org/cmd/go/#hdr-Testing_flags)

- Az aktuális könyvtárban található csomag tesztelése:

`go test`

- \[v\]erbosely teszteli az aktuális könyvtárban található csomagot:

`go test -v`

- Az aktuális könyvtárban és az összes alkönyvtárban található csomagok tesztelése (figyeljünk a `...`):

`go test -v ./...`

- Az aktuális könyvtárban lévő csomag tesztelése és az összes benchmark futtatása:

`go test -v -bench .`

- Az aktuális könyvtárban lévő csomag tesztelése és az összes benchmark futtatása 50 másodpercig:

`go test -v -bench . -benchtime {{50s}}`

- A csomag tesztelése lefedettségi elemzéssel:

`go test -cover`
