# srm

> Fájlok vagy könyvtárak biztonságos eltávolítása. A meglévő adatokat egy vagy több alkalommal felülírja. Az rm helyettesítője. További információ: <http://srm.sourceforge.net/srm.html>.

- Egy fájl eltávolítása egyszeri, véletlenszerű adatokkal történő felülírás után:

`srm -s {{path/to/file}}`

- Egy fájl eltávolítása hét véletlenszerű adatokkal történő felülírás után:

`srm -m {{path/to/file}}`

- Rekurzívan eltávolít egy könyvtárat és annak tartalmát, minden egyes fájlt véletlenszerű adatokkal egy menetben felülírva:

`srm -r -s {{path/to/directory}}`

- Minden eltávolítás előtt kérdezzen:

`srm -i {{\*}}`
