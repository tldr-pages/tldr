# ogrinfo

> Az OGR által támogatott adatforrással kapcsolatos információk listázása. További információ: <https://gdal.org/programs/ogrinfo.html>.

- Támogatott formátumok felsorolása:

`ogrinfo --formats`

- Az adatforrás rétegeinek listázása:

`ogrinfo {{path/to/input.gpkg}}`

- Részletes információk lekérdezése egy adatforrás egy adott rétegéről:

`ogrinfo {{path/to/input.gpkg}} {{layer_name}}`

- Összefoglaló információk megjelenítése egy adatforrás egy adott rétegéről:

`ogrinfo -so {{path/to/input.gpkg}} {{layer_name}}`

- Az adatforrás összes rétegének összefoglalójának megjelenítése:

`ogrinfo -so -al {{path/to/input.gpkg}}`

- A feltételnek megfelelő jellemzők részletes információinak megjelenítése:

`ogrinfo -where '{{attribute_name > 42}}' {{path/to/input.gpkg}} {{layer_name}}`

- Az adatforrás egy rétegének frissítése SQL segítségével:

`ogrinfo {{path/to/input.geojson}} -dialect SQLite -sql "{{UPDATE input SET attribute_name = 'foo'}}"`
