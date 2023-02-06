# locate

> A fájlnevek gyors megtalálása. További információ: <https://manned.org/locate>.

- Keressen mintát az adatbázisban. Megjegyzés: az adatbázis időszakonként (általában hetente vagy naponta) újraszámlálásra kerül:

`locate {{pattern}}`

- Keressen egy fájlt a pontos fájlnév alapján (a globbing karaktereket nem tartalmazó mintát a `*pattern*` értelmezi):

`locate */{{filename}}`

- Az adatbázis újraszámítása. Erre akkor van szükség, ha a nemrég hozzáadott fájlokat szeretné megtalálni:

`sudo updatedb`
