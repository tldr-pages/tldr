# jest

> Konfigurációmentes JavaScript tesztelési platform. További információ: <https://jestjs.io>.

- Az összes elérhető teszt futtatása:

`jest`

- A megadott fájlok tesztkészleteinek futtatása:

`jest {{path/to/file1}} {{path/to/file2}}`

- A tesztkészletek futtatása az aktuális és az alkönyvtárakban található olyan fájlokból, amelyek elérési útvonala megfelel a megadott reguláris kifejezésnek:

`jest {{regular_expression1}} {{regular_expression2}}`

- Azoknak a teszteknek a futtatása, amelyek neve megfelel a megadott reguláris kifejezésnek:

`jest --testNamePattern {{regular_expression}}`

- Egy adott forrásfájlhoz kapcsolódó tesztcsomagok futtatása:

`jest --findRelatedTests {{path/to/source_file.js}}`

- Az összes nem lekötött fájlhoz kapcsolódó tesztcsomagok futtatása:

`jest --onlyChanged`

- A fájlok változásainak figyelése és a kapcsolódó tesztek automatikus újrafuttatása:

`jest --watch`

- Súgó megjelenítése:

`jest --help`
