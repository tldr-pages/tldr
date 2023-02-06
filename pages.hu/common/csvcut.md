# csvcut

> CSV fájlok szűrése és csonkítása. Mint a Unix `cut` parancsa, de táblázatos adatokhoz. A csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- Az összes oszlop indexének és nevének nyomtatása:

`csvcut -n {{data.csv}}`

- Az első és a harmadik oszlopok kivonása:

`csvcut -c {{1,3}} {{data.csv}}`

- Kivonatolja az összes oszlopot a negyedik **kivételével**:

`csvcut -C {{4}} {{data.csv}}`

- Kivonatolja az "id" és "keresztnév" nevű oszlopokat (ebben a sorrendben):

`csvcut -c {{id,"first name"}} {{data.csv}}`
