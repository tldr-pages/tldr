# size

> Megjeleníti a bináris fájlokban lévő szakaszok méretét. További információ: <https://sourceware.org/binutils/docs/binutils/size.html>.

- Megjeleníti a szakaszok méretét egy adott objektum- vagy futtatható fájlban:

`size {{path/to/file}}`

- Megjeleníti a szakaszok méretét egy adott objektumban vagy futtatható fájlban \[o\]ctal:

`size {{-o|--radix=8}} {{path/to/file}}`

- A szakaszok méretének megjelenítése egy adott objektumban vagy végrehajtható fájlban \[d\]ecimalban:

`size {{-d|--radix=10}} {{path/to/file}}`

- A szakaszok méretének megjelenítése egy adott objektumban vagy végrehajtható fájlban he\[x\]adecimális értékben:

`size {{-x|--radix=16}} {{path/to/file}}`
