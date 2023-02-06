# rabin2

> Információszerzés bináris fájlokról (ELF, PE, Java CLASS, Mach-O) - szimbólumok, szakaszok, linkelt könyvtárak, stb. A `radare2` oldalon található. További információ: <https://manned.org/rabin2>.

- Általános információk megjelenítése a bináris fájlról (architektúra, típus, endianness):

`rabin2 -I {{path/to/binary}}`

- Kapcsolódó könyvtárak megjelenítése:

`rabin2 -l {{path/to/binary}}`

- Könyvtárakból importált szimbólumok megjelenítése:

`rabin2 -i {{path/to/binary}}`

- A binárisban található karakterláncok megjelenítése:

`rabin2 -z {{path/to/binary}}`

- A kimenet megjelenítése JSON-ban:

`rabin2 -j -I {{path/to/binary}}`
