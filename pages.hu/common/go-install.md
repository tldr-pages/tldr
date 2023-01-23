# go install

> Az importálási útvonalak által megnevezett csomagok fordítása és telepítése. További információ: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- Az aktuális csomag fordítása és telepítése:

`go install`

- Egy adott helyi csomag lefordítása és telepítése:

`go install {{path/to/package}}`

- Egy program legújabb verziójának telepítése, figyelmen kívül hagyva az aktuális könyvtárban található `go.mod` címet:

`go install {{golang.org/x/tools/gopls}}@{{latest}}`

- Egy program telepítése a `go.mod` által kiválasztott verzióval az aktuális könyvtárban:

`go install {{golang.org/x/tools/gopls}}`
