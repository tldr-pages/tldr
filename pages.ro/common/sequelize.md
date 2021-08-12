# sequelize

> Node.js ORM pe bază de promisiune pentru Postgres, MySQL, MariaDB, SQLite şi Microsoft SQL Server.
> Mai multe informaţii: <https://sequelize.org/>

- Creați un model cu 3 câmpuri și un fișier de migrare:

`sequelize model:generate --name {{table_name}} --attributes {{field1:integer,field2:string,field3:boolean}}`

- Rulați fișierul de migrare:

`sequelize db:migrate`

- Reveniți toate migrațiile:

`sequelize db:migrate:undo:all`

- Creați un fișier de semințe cu numele specificat pentru a popula baza de date:

`sequelize seed:generate --name {{seed_filename}}`

- Populați baza de date folosind toate fișierele de semințe:

`sequelize db:seed:all`
