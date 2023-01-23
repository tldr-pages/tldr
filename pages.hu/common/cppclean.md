# cppclean

> Fel nem használt kód keresése C++ projektekben. További információ: <https://github.com/myint/cppclean>.

- Futtatás egy projekt könyvtárában:

`cppclean {{path/to/project}}`

- Futtatás egy olyan projekten, ahol a fejlécek a `inc1/` és a `inc2/` könyvtárakban vannak:

`cppclean {{path/to/project}} --include-path={{inc1}} --include-path={{inc2}}`

- Futtatás egy adott fájlon `main.cpp`:

`cppclean {{main.cpp}}`

- Futtatás az aktuális könyvtáron, kivéve a "build" könyvtárat:

`cppclean {{.}} --exclude={{build}}`
