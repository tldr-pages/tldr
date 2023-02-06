# plocate

> A fájlnevek gyors megtalálása. Az új fájlok felvételéhez feltétlenül futtassa a `sudo updatedb`. További információ: <https://plocate.sesse.net>.

- Keressen mintákat az adatbázisban (időszakonként újraszámolva):

`plocate {{pattern}}`

- Keressen egy fájlt a pontos fájlnév alapján (a globbing karaktereket nem tartalmazó mintát a `*pattern*` értelmezi):

`plocate */{{filename}}`
