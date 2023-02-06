# lrzuntar

> A `lrunzip` csomagolása a könyvtárak dekompressziójának egyszerűsítésére. Lásd még: `lrztar` `lrzip` További információ: <https://manned.org/lrzuntar>.

- Dekompresszió egy fájlból az aktuális könyvtárba:

`lrzuntar {{path/to/archive.tar.lrz}}`

- Dekompresszió egy fájlból az aktuális könyvtárba egy adott számú processzorszál felhasználásával:

`lrzuntar -p {{8}} {{path/to/archive.tar.lrz}}`

- Dekompresszió egy fájlból az aktuális könyvtárba, és a már létező elemek csendes felülírása:

`lrzuntar -f {{archive.tar.lrz}}`

- A kimeneti útvonal megadása:

`lrzuntar -O {{path/to/directory}} {{archive.tar.lrz}}`

- A tömörített fájl törlése a tömörítés után:

`lrzuntar -D {{path/to/archive.tar.lrz}}`
