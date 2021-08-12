# ogr2ogr

> Conversia datelor Caracteristici simple între formatele de fișier.
> Mai multe informaţii: <https://gdal.org/programs/ogr2ogr.html#ogr2ogr>

- Conversia unui fișier Shapefile într-un GeoPackage:

`ogr2ogr -f GPKG {{output}}.gpkg {{input}}.shp`

- Modificarea sistemului de referință de coordonate al unei GeoPackage de la `EPSG:4326` la `EPSG: 3857`:

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{output}}.gpkg {{input}}.gpkg`

- Conversia unui fișier CSV într-un GeoPackage, specificând numele coloanelor de coordonate și atribuind un sistem de referință de coordonate:

`ogr2ogr -f GPKG {{output}}.gpkg {{input}}.csv -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}`

- Încărcarea unei GeoPackage într-o bază de date PostGIS:

`ogr2ogr -f "PostgreSQL" PG:dbname="{{database_name}}" {{input}}.gpkg`

- Clip straturi ale unui fişier GeoPackage în caseta de încadrare dată:

`ogr2ogr -spat {{min_x}} {{min_y}} {{max_x}} {{max_y}} -f GPKG {{output}}.gpkg {{input}}.gpkg`
