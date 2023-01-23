# parquet-tools

> Eszköz a Parquet fájl megjelenítésére, vizsgálatára és manipulálására. További információ: <https://github.com/apache/parquet-mr/tree/master/parquet-tools-deprecated>.

- Egy Parquet fájl tartalmának megjelenítése:

`parquet-tools cat {{path/to/parquet}}`

- Egy Parquet fájl első néhány sorának megjelenítése:

`parquet-tools head {{path/to/parquet}}`

- Egy Parquet fájl sémájának kinyomtatása:

`parquet-tools schema {{path/to/parquet}}`

- Egy Parquet fájl metaadatainak nyomtatása:

`parquet-tools meta {{path/to/parquet}}`

- Egy Parquet-fájl tartalmának és metaadatainak nyomtatása:

`parquet-tools dump {{path/to/parquet}}`

- Több Parquet-fájl összevonása a célfájlba:

`parquet-tools merge {{path/to/parquet1}} {{path/to/parquet2}} {{path/to/target_parquet}}`

- A sorok számának nyomtatása egy Parquet-fájlban:

`parquet-tools rowcount {{path/to/parquet}}`

- Egy Parquet-fájl oszlop- és eltolási indexeinek nyomtatása:

`parquet-tools column-index {{path/to/parquet}}`
