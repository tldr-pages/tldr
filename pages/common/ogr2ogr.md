# ogr2ogr

> Convert Simple Features data between file formats.
> More information: <https://gdal.org/programs/ogr2ogr.html#ogr2ogr>.

- Convert a Shapefile into a GeoPackage:

`ogr2ogr -f GPKG {{output}}.gpkg {{input}}.shp`

- Change coordinate reference system of a GeoPackage from `EPSG:4326` to `EPSG:3857`:

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{output}}.gpkg {{input}}.gpkg`

- Convert a CSV file into a GeoPackage, specifying the names of the coordinate columns and assigning a coordinate reference system:

`ogr2ogr -f GPKG {{output}}.gpkg {{input}}.csv -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}`

- Load a GeoPackage into a PostGIS database:

`ogr2ogr -f "PostgreSQL" PG:dbname="{{database_name}}" {{input}}.gpkg`

- Clip layers of a GeoPackage file to the given bounding box:

`ogr2ogr -spat {{min_x}} {{min_y}} {{max_x}} {{max_y}} -f GPKG {{output}}.gpkg {{input}}.gpkg`
