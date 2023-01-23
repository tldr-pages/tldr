# strip

> A szimbólumok eltávolítása a végrehajtható programokból vagy objektumfájlokból. További információ: <https://manned.org/strip>.

- A bemeneti fájl cseréje a lecsupaszított változatra:

`strip {{path/to/file}}`

- Szimbólumok eltávolítása egy fájlból, a kimenetet egy adott fájlba mentve:

`strip {{path/to/input_file}} -o {{path/to/output_file}}`

- Csak a hibakeresési szimbólumok eltávolítása:

`strip --strip-debug {{path/to/file.o}}`
