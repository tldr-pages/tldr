# lzip

> Az Lzip egy veszteségmentes adattömörítő, amelynek felhasználói felülete hasonló a `gzip` vagy a `bzip2`.
> Az Lzip a "Lempel-Ziv-Markovchain-Algorithm "z (LZMA) stream formátum egyszerűsített formáját használja, és 3 faktoros integritás-ellenőrzést biztosít az interoperabilitás maximalizálása és a biztonság optimalizálása érdekében.
> További információ: <https://www.nongnu.org/lzip>.

- Egy fájl archiválása, kicserélve azt egy tömörített verzióra:

`lzip {{path/to/file}}`

- Archiváljon egy fájlt, megtartva a bemeneti fájlt:

`lzip -k {{path/to/file}}`

- Archiváljon egy fájlt a legjobb tömörítéssel (9. szint=9):

`lzip -k {{path/to/file}} --best`

- Archiváljon egy fájlt a legnagyobb sebességgel (szint=0):

`lzip -k {{path/to/file}} --fast`

- A tömörített fájl integritásának tesztelése:

`lzip --test {{path/to/archive.lz}}`

- Egy fájl kitömörítése, az eredeti tömörítetlen verzióval való helyettesítése:

`lzip -d {{path/to/archive.lz}}`

- Egy fájl kicsomagolása az archívum megtartásával:

`lzip -d -k {{path/to/archive.lz}}`

- Az archívumban lévő fájlok listázása és a tömörítési statisztikák megjelenítése:

`lzip --list {{path/to/archive.lz}}`
