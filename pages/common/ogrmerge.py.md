# ogrmerge.py

> Merge several vector datasets into a single one.
> More information: <https://gdal.org/programs/ogrmerge.html>.

- Create a GeoPackage with a layer for each input Shapefile:

`ogrmerge.py -f {{GPKG}} -o {{path/to/merged}}.gpkg {{path/to/}}*.shp`

- Create a virtual datasource (VRT) with a layer for each input Shapefile:

`ogrmerge.py -f {{VRT}} -o {{merged}}.vrt {{path/to/}}*.shp`

- Concatenate three vector datasets into one:

`ogrmerge.py -single -o {{path/to/output.geojson}} {{path/to/input_a.geojson}} {{path/to/input_b.geojson}} {{path/to/input_c.geojson}}`

- Concatenate two vector datasets and store source name of dataset in attribute 'source_name':

`ogrmerge.py -single -o {{path/to/output.geojson}} {{path/to/input_a.geojson}} {{path/to/input_b.geojson}} -src_layer_field_name country {{source_name}}`
