# ulimit

> Felhasználói korlátok lekérése és beállítása. További információ: <https://manned.org/ulimit>.

- Az összes felhasználói limit tulajdonságainak lekérdezése:

`ulimit -a`

- Az egyidejűleg megnyitott fájlok számának kemény korlátjának lekérdezése:

`ulimit -H -n`

- Az egyidejűleg megnyitott fájlok számának puha korlátjának lekérdezése:

`ulimit -S -n`

- Felhasználónkénti maximális folyamatlimit beállítása:

`ulimit -u 30`
