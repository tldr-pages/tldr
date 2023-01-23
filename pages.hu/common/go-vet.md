# go vet

> A Go forráskód ellenőrzése és a gyanús konstrukciók jelentése (pl. lint a Go forrásfájlok). A Go vet egy nem nulla kilépési kódot ad vissza, ha problémákat talál; nullás kilépési kódot ad vissza, ha nem talál problémákat. További információ: <https://pkg.go.dev/cmd/vet>.

- Az aktuális könyvtárban lévő Go csomag ellenőrzése:

`go vet`

- A Go csomag ellenőrzése a megadott elérési útvonalban:

`go vet {{path/to/file_or_directory}}`

- A go vet segítségével futtatható elérhető ellenőrzések listája:

`go tool vet help`

- Egy adott ellenőrzés részleteinek és zászlóinak megtekintése:

`go tool vet help {{check_name}}`

- A hibás sorok és a környező kontextus N sorának megjelenítése:

`go vet -c={{N}}`

- Elemzés és hibák kimenete JSON formátumban:

`go vet -json`
