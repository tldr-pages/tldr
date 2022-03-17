# ogrmerge.py

> Merge several vector datasets into a single one.
> More information: <https://gdal.org/programs/ogrmerge.html>.

- Create a GeoPackage with a layer for each input Shapefile:

`ogrmerge.py -f {{GPKG}} -o {{path/to/output.gpkg}} {{path/to/input1.shp path/to/input2.shp ...}}`

- Create a virtual datasource (VRT) with a layer for each input GeoJSON:

`ogrmerge.py -f {{VRT}} -o {{path/to/output}}.vrt {{path/to/input_a.geojson path/to/input_b.geojson ...}}`

- Concatenate two vector datasets and store source name of dataset in attribute 'source_name':

`ogrmerge.py -single -o {{path/to/output.geojson}} -src_layer_field_name country {{source_name}} {{path/to/input_a.shp path/to/input_b.shp ...}}`
