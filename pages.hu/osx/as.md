# as

> Hordozható GNU asszembler. Elsősorban a `gcc` kimenetének összerakására szolgál, hogy a `ld` használhassa. További információ: <https://www.unix.com/man-page/osx/1/as/>.

- Összeállít egy fájlt, a kimenetet a `a.out` címre írja:

`as {{file.s}}`

- A kimenet összerakása egy adott fájlba:

`as {{file.s}} -o {{out.o}}`

- Gyorsabb kimenetet generál a szóközök és a megjegyzések előfeldolgozásának kihagyásával. (Csak megbízható fordítóprogramok esetén használható):

`as -f {{file.s}}`

- Adott elérési útvonal felvétele a `.include` direktívákban megadott fájlok keresésére szolgáló könyvtárak listájába:

`as -I {{path/to/directory}} {{file.s}}`
