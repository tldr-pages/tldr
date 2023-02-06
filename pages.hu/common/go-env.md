# go env

> A Go toolchain által használt környezeti változók kezelése. További információ: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- Az összes környezeti változó megjelenítése:

`go env`

- Egy adott környezeti változó megjelenítése:

`go env {{GOPATH}}`

- Egy környezeti változó értékének beállítása:

`go env -w {{GOBIN}}={{path/to/directory}}`

- Egy környezeti változó értékének visszaállítása:

`go env -u {{GOBIN}}`
