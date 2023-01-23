# go build

> Go források összeállítása. További információ: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- Fordítson le egy 'package main' fájlt (a kimenet a kiterjesztés nélküli fájlnév lesz):

`go build {{path/to/main.go}}`

- Compile, a kimeneti fájlnév megadásával:

`go build -o {{path/to/binary}} {{path/to/source.go}}`

- Compile a package:

`go build -o {{path/to/binary}} {{path/to/package}}`

- Egy fő csomag lefordítása futtathatóvá, lehetővé téve az adatverseny-felismerést:

`go build -race -o {{path/to/executable}} {{path/to/main/package}}`
