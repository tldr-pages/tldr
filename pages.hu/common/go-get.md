# go get

> Függőségi csomag hozzáadása, vagy csomagok letöltése hagyományos GOPATH módban. További információ: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- Egy megadott csomag hozzáadása a `go.mod` oldalhoz modul-módban, vagy a csomag telepítése GOPATH-módban:

`go get {{example.com/pkg}}`

- Módosítsa a csomagot egy adott verzióval modul-tudatos módban:

`go get {{example.com/pkg}}@{{v1.2.3}}`

- Megadott csomag eltávolítása:

`go get {{example.com/pkg}}@{{none}}`
