# larasail

> CLI eszköz a Laravel kezelésére a Digital Ocean szerverein. További információ: <https://github.com/thedevdojo/larasail>.

- Állítsa be a szervert a Laravel függőségekkel az alapértelmezett PHP verzióval:

`larasail setup`

- A kiszolgáló beállítása a Laravel függőségekkel egy adott PHP-verzió használatával:

`larasail setup {{php71}}`

- Új Laravel webhely hozzáadása:

`larasail host {{domain}} {{path/to/site_directory}}`

- A Larasail felhasználói jelszó lekérdezése:

`larasail pass`

- A Larasail MySQL-jelszó lekérdezése:

`larasail mysqlpass`
