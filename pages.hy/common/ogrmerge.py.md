# ogrmerge.py

> Միավորել մի քանի վեկտորային տվյալների հավաքածուներ մեկ մեկի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/ogrmerge.html>:.

- Ստեղծեք GeoPackage շերտով յուրաքանչյուր մուտքագրված Shapefile-ի համար.:

`ogrmerge.py -f {{GPKG}} -o {{path/to/output.gpkg}} {{path/to/input1.shp path/to/input2.shp ...}}`

- Ստեղծեք վիրտուալ տվյալների աղբյուր (VRT) շերտով յուրաքանչյուր մուտքագրման համար GeoJSON:

`ogrmerge.py -f {{VRT}} -o {{path/to/output.vrt}} {{path/to/input1.geojson path/to/input2.geojson ...}}`

- Միացրեք երկու վեկտորային տվյալների հավաքածուներ և պահեք տվյալների աղբյուրի անունը «source_name» հատկանիշում.:

`ogrmerge.py -single -f {{GeoJSON}} -o {{path/to/output.geojson}} -src_layer_field_name country {{source_name}} {{path/to/input1.shp path/to/input2.shp ...}}`
