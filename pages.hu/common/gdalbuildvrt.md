# gdalbuildvrt

> Virtuális adatkészletek létrehozása meglévő adatkészletek listájából. További információ: <https://gdal.org/programs/gdalbuildvrt.html>.

- Virtuális mozaik készítése egy könyvtárban található összes TIFF fájlból:

`gdalbuildvrt {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`

- Virtuális mozaik készítése olyan fájlokból, amelyek neve egy szöveges fájlban van megadva:

`gdalbuildvrt -input_file_list {{path/to/list.txt}} {{path/to/output.vrt}}`

- Virtuális RGB-mozaik készítése 3 egysávos bemeneti fájlból:

`gdalbuildvrt -separate {{path/to/rgb.vrt}} {{path/to/red.tif}} {{path/to/green.tif}} {{path/to/blue.tif}}`

- Készítsen virtuális mozaikot kék háttérszínnel (RGB: 0 0 255):

`gdalbuildvrt -hidenodata -vrtnodata "{{0 0 255}}" {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`
