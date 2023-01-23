# uncrustify

> C, C++, C#, D, Java és Pawn forráskódformázó. További információ: <https://github.com/uncrustify/uncrustify>.

- Egyetlen fájl formázása:

`uncrustify -f {{path/to/file.cpp}} -o {{path/to/output.cpp}}`

- Olvassa be a fájlneveket a `stdin` címről, és készítsen biztonsági másolatot, mielőtt visszaírja a kimenetet az eredeti fájlútvonalakra:

`find . -name "*.cpp" | uncrustify -F - --replace`

- Ne készítsen biztonsági mentéseket (hasznos, ha a fájlok verziókezelő alatt állnak):

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- Használjon egyéni konfigurációs fájlt, és írja az eredményt a `stdout` címre:

`uncrustify -c {{path/to/uncrustify.cfg}} -f {{path/to/file.cpp}}`

- Egy konfigurációs változó értékének explicit beállítása:

`uncrustify --set {{option}}={{value}}`

- Új konfigurációs fájl létrehozása:

`uncrustify --update-config -o {{path/to/new.cfg}}`
