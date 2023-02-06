# go mod

> Modul karbantartás. További információ: <https://golang.org/cmd/go/#hdr-Module_maintenance>.

- Új modul inicializálása az aktuális könyvtárban:

`go mod init {{moduleName}}`

- Modulok letöltése a helyi gyorsítótárba:

`go mod download`

- Hiányzó és nem használt modulok hozzáadása és eltávolítása:

`go mod tidy`

- Ellenőrizze, hogy a függőségek rendelkeznek-e az elvárt tartalommal:

`go mod verify`

- Az összes függőség forrásának másolása a szállító könyvtárba:

`go mod vendor`
