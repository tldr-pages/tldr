# ditto

> Fájlok és könyvtárak másolása. További információ: <https://ss64.com/osx/ditto.html>.

- A célkönyvtár tartalmának felülírása a forráskönyvtár tartalmával:

`ditto {{path/to/source}} {{path/to/destination}}`

- Minden másolandó fájlhoz kiír egy sort a terminál ablakba:

`ditto -V {{path/to/source}} {{path/to/destination}}`

- Adott fájl vagy könyvtár másolása az eredeti fájljogosultságok megtartása mellett:

`ditto -rsrc {{path/to/source}} {{path/to/destination}}`
