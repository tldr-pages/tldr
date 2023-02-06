# wp

> A hivatalos parancssori felület a WordPress példányok kezelésére. További információ: <https://wp-cli.org/>.

- Az operációs rendszer, a shell, a PHP és a WP-CLI (`wp`) telepítésével kapcsolatos információk kinyomtatása:

`wp --info`

- WP-CLI frissítése:

`wp cli update`

- Friss WordPress-telepítés letöltése az aktuális könyvtárba, opcionálisan megadva a nyelvterületet:

`wp core download --locale={{locale}}`

- Alapvető `wpconfig` fájl létrehozása (feltételezve, hogy az adatbázis a `localhost`):

`wp config create --dbname={{dbname}} --dbuser={{dbuser}} --dbpass={{dbpass}}`

- WordPress plugin telepítése és aktiválása:

`wp plugin install {{plugin}} --activate`

- Egy karakterlánc összes példányának cseréje az adatbázisban:

`wp search-replace {{old_string}} {{new_string}}`

- Egy WordPress Extended RSS (WXR) fájl tartalmának importálása:

`wp import {{path/to/file.xml}}`
