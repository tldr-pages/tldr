# gunzip

> Fájl(ok) kicsomagolása gzip (.gz) archívumból. További információ: <https://manned.org/gunzip>.

- Fájl kivonása egy archívumból, az eredeti fájl helyettesítésével, ha az létezik:

`gunzip {{archive.tar.gz}}`

- Fájl kivonása egy célállomásra:

`gunzip --stdout {{archive.tar.gz}} > {{archive.tar}}`

- Fájl kivonása és az archív fájl megtartása:

`gunzip --keep {{archive.tar.gz}}`

- Egy tömörített fájl tartalmának listázása:

`gunzip --list {{file.txt.gz}}`

- Az archívum kicsomagolása a `stdin` oldalról:

`cat {{path/to/archive.gz}} | gunzip`
