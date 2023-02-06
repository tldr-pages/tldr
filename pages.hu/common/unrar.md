# unrar

> RAR-archívumok kibontása. További információ: <https://manned.org/unrar>.

- A fájlok eredeti könyvtárstruktúrával történő kibontása:

`unrar x {{compressed.rar}}`

- Fájlok kibontása egy megadott elérési útvonalra az eredeti könyvtárstruktúrával:

`unrar x {{compressed.rar}} {{path/to/extract}}`

- Fájlok kibontása az aktuális könyvtárba, az archívum könyvtárszerkezetének elvesztésével:

`unrar e {{compressed.rar}}`

- Az archívumfájlon belüli egyes fájlok integritásának tesztelése:

`unrar t {{compressed.rar}}`

- Az archívumfájlon belüli fájlok listázása a fájl kicsomagolása nélkül:

`unrar l {{compressed.rar}}`
