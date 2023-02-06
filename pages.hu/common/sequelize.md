# sequelize

> Promise-alapú Node.js ORM a Postgres, MySQL, MariaDB, SQLite és Microsoft SQL Server számára. További információ: <https://sequelize.org/>.

- Hozzon létre egy modellt 3 mezővel és egy migrációs fájllal:

`sequelize model:generate --name {{table_name}} --attributes {{field1:integer,field2:string,field3:boolean}}`

- Futtassa a migrációs fájlt:

`sequelize db:migrate`

- Az összes migráció visszaállítása:

`sequelize db:migrate:undo:all`

- Hozzon létre egy magfájlt a megadott névvel az adatbázis feltöltéséhez:

`sequelize seed:generate --name {{seed_filename}}`

- Az adatbázis feltöltése az összes magfájl felhasználásával:

`sequelize db:seed:all`
