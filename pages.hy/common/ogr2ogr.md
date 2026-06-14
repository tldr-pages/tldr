# ogr2ogr

> Փոխարկել աշխարհատարածական վեկտորային տվյալները ֆայլի ձևաչափերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/ogr2ogr.html>:.

- Փոխակերպեք Shapefile-ը GeoPackage-ի.:

`ogr2ogr -f GPKG {{path/to/output.gpkg}} {{path/to/input.shp}}`

- Կրճատել GeoJSON-ը պայմանին համապատասխանող հատկանիշների.:

`ogr2ogr -where '{{myProperty > 42}}' -f {{GeoJSON}} {{path/to/output.geojson}} {{path/to/input.geojson}}`

- Փոխեք GeoPackage-ի կոորդինատային հղման համակարգը `EPSG:4326`-ից `EPSG:3857`:

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{path/to/output.gpkg}} {{path/to/input.gpkg}}`

- Փոխակերպեք CSV ֆայլը GeoPackage-ի, նշելով կոորդինատային սյունակների անունները և նշանակելով կոորդինատային հղման համակարգ.:

`ogr2ogr -f GPKG {{path/to/output.gpkg}} {{path/to/input.csv}} -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}`

- Ներբեռնեք GeoPackage PostGIS տվյալների բազայում.:

`ogr2ogr -f PostgreSQL PG:dbname="{{database_name}}" {{path/to/input.gpkg}}`

- Սեղմեք GeoPackage ֆայլի շերտերը տվյալ սահմանափակող վանդակում.:

`ogr2ogr -spat {{min_x}} {{min_y}} {{max_x}} {{max_y}} -f GPKG {{path/to/output.gpkg}} {{path/to/input.gpkg}}`
