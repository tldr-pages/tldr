# ogr2ogr

> Convert Simple Features data between file formats.
> More information: <https://gdal.org/programs/ogr2ogr.html#ogr2ogr>.

- Convert a Shapefile into a GeoPackage:

`ogr2ogr -f GPKG {{output}}.gpkg {{input}}.shp`

- Reproject a GeoPackage from `EPSG:4326` to `EPSG:3857` coordinate reference system:

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{output}}.gpkg {{input}}.gpkg`

- Convert a CSV file into a GeoPackage, specifying the names of the coordinate columns and assigning a coordinate reference system:

`ogr2ogr -f GPKG {{output}}.gpkg {{input}}.csv -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}`

- Load a GeoPackage into a PostGIS database:

`ogr2ogr -f "PostgreSQL" PG:dbname="{{my_database}}" {{input}}.gpkg`

- Filter GeoPackage by bounding box (<xmin> <ymin> <xmax> <ymax>):

`ogr2ogr -spat {{-13.931}} {{34.886}} {{46.23}} {{74.12}} -f GPKG {{output}}.gpkg {{input}}.gpkg`
