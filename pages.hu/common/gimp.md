# gimp

> GNU képmanipuláló program. Lásd még: `krita`. További információ: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- Indítsa el a GIMP-et:

`gimp`

- Meghatározott fájlok megnyitása:

`gimp {{path/to/image1 path/to/image2 ...}}`

- Meghatározott fájlok megnyitása új ablakban:

`gimp --new-instance {{path/to/image1 path/to/image2 ...}}`

- Indítás kezdőképernyő nélkül:

`gimp --no-splash`

- Hibák és figyelmeztetések kiírása a konzolra ahelyett, hogy párbeszédpanelben jelenítené meg őket:

`gimp --console-messages`

- A hibakeresési jelkezelők engedélyezése:

`gimp --debug-handlers`
