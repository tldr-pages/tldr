# goimports

> A Go import sorok frissítése, a hiányzó sorok hozzáadása és a nem hivatkozott sorok eltávolítása. További információ: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Az elkészült import forrásfájl megjelenítése:

`goimports {{path/to/file}}.go`

- Az eredmény visszaírása a szabványos kimenet helyett a forrásfájlba:

`goimports -w {{path/to/file}}.go`

- A diffs megjelenítése és az eredmény visszaírása a forrásfájlba:

`goimports -w -d {{path/to/file}}.go`

- Import prefix string beállítása a 3rd-party csomagok után (vesszővel elválasztott lista):

`goimports -local {{path/to/package}} {{path/to/file}}.go`
