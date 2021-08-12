# go build

> Compilarea surselor Go.
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>

- Compilarea unui fișier:

`go build {{path/to/main.go}}`

- Compilați, specificând numele fișierului de ieșire:

`go build -o {{path/to/binary}} {{path/to/source.go}}`

- Compilarea unui pachet:

`go build -o {{path/to/binary}} {{path/to/package}}`

- Compilați un pachet principal într-un executabil, cu detectarea cursei de date:

`go build -race -o {{path/to/executable}} {{path/to/main/package}}`
