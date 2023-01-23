# ogrmerge.py

> Több vektoros adatkészlet egyesítése egyetlen vektoros adatkészletté. További információ: <https://gdal.org/programs/ogrmerge.html>.

- Hozzon létre egy GeoPackage-et, amely minden egyes bemeneti Shapefile-hoz egy réteget tartalmaz:

`ogrmerge.py -f {{GPKG}} -o {{path/to/output.gpkg}} {{path/to/input1.shp path/to/input2.shp ...}}`

- Hozzon létre egy virtuális adatforrást (VRT) egy réteggel minden egyes bemeneti GeoJSON-hoz:

`ogrmerge.py -f {{VRT}} -o {{path/to/output.vrt}} {{path/to/input1.geojson path/to/input2.geojson ...}}`

- Két vektoros adatkészlet összekapcsolása és az adatkészlet forrásnevének tárolása a "source_name" attribútumban:

`ogrmerge.py -single -f {{GeoJSON}} -o {{path/to/output.geojson}} -src_layer_field_name country {{source_name}} {{path/to/input1.shp path/to/input2.shp ...}}`
