# ogr2ogr

> Térbeli vektoros adatok konvertálása fájlformátumok között. További információ: <https://gdal.org/programs/ogr2ogr.html>.

- Shapefile átalakítása GeoPackage-é:

`ogr2ogr -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.shp`

- Egy GeoJSON redukciója egy feltételnek megfelelő jellemzőkre:

`ogr2ogr -where '{{myProperty > 42}}' -f {{GeoJSON}} {{path/to/output.geojson}} {{path/to/input.geojson}}`

- Egy GeoPackage koordináta-referenciarendszerének módosítása `EPSG:4326` -ról `EPSG:3857`-re:

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.gpkg`

- Egy CSV-fájl GeoPackage-be konvertálása a koordinátaoszlopok nevének megadásával és a koordináta-referenciarendszer hozzárendelésével:

`ogr2ogr -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.csv -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}`

- GeoPackage betöltése PostGIS adatbázisba:

`ogr2ogr -f PostgreSQL PG:dbname="{{database_name}}" {{path/to/input}}.gpkg`

- A GeoPackage fájl rétegeinek a megadott határoló kerethez való vágása:

`ogr2ogr -spat {{min_x}} {{min_y}} {{max_x}} {{max_y}} -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.gpkg`
