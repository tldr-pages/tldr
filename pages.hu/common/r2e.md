# r2e

> RSS-feedek továbbítása egy e-mail címre. Konfigurált `sendmail` vagy smtp beállítás szükséges. További információ: <https://github.com/rss2email/rss2email>.

- Új feed-adatbázis létrehozása, amely e-mailt küld egy e-mail címre:

`r2e new {{email_address}}`

- Feliratkozás egy feedre:

`r2e add {{feed_name}} {{feed_URI}}`

- Új történetek küldése egy e-mail címre:

`r2e run`

- Az összes feed listázása:

`r2e list`

- Egy megadott indexen lévő feed törlése:

`r2e delete {{index}}`
