# go

> Eszköz a go forráskód kezelésére. Néhány alparancsnak, mint például a `go build`, saját használati dokumentációja van. További információ: <https://golang.org>.

- Letölt és telepít egy csomagot, amelyet az importálási útvonala határoz meg:

`go get {{package_path}}`

- Egy forrásfájl lefordítása és futtatása (tartalmaznia kell egy `main` csomagot):

`go run {{file}}.go`

- Egy forrásfájl lefordítása egy megnevezett futtatható fájlba:

`go build -o {{executable}} {{file}}.go`

- Az aktuális könyvtárban lévő csomag lefordítása:

`go build`

- Az aktuális csomag összes tesztesetének végrehajtása (a fájloknak a `_test.go` végződéssel kell végződniük):

`go test`

- Az aktuális csomag fordítása és telepítése:

`go install`

- Új modul inicializálása az aktuális könyvtárban:

`go mod init {{module_name}}`
