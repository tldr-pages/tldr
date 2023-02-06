# rails db

> Különböző adatbázisokkal kapcsolatos alparancsok a Ruby on Rails számára. További információ: <https://guides.rubyonrails.org/command_line.html>.

- Adatbázisok létrehozása, a séma betöltése és inicializálás magadatokkal:

`rails db:setup`

- Hozzáférés az adatbázis konzoljához:

`rails db`

- Az aktuális környezetben definiált adatbázisok létrehozása:

`rails db:create`

- Az aktuális környezetben definiált adatbázisok megsemmisítése:

`rails db:drop`

- Függőben lévő migrációk futtatása:

`rails db:migrate`

- Az egyes migrációs fájlok állapotának megtekintése:

`rails db:migrate:status`

- A legutóbbi áttelepítés visszavétele:

`rails db:rollback`

- Az aktuális adatbázis feltöltése a `db/seeds.rb` oldalon meghatározott adatokkal:

`rails db:seed`
