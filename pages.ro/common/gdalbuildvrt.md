# gdalbuildvrt

> Construiți seturi de date virtuale dintr-o listă de seturi de date existente.
> Mai multe informaţii: <https://gdal.org/programs/gdalbuildvrt.html>

- Faceți un mozaic virtual din toate fișierele TIFF conținute într-un director:

`gdalbuildvrt {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`

- Faceți un mozaic virtual din fișiere al căror nume este specificat într-un fișier text:

`gdalbuildvrt -input_file_list {{path/to/list.txt}} {{path/to/output.vrt}}`

- Faceți un mozaic virtual RGB din 3 fișiere de intrare cu o singură bandă:

`gdalbuildvrt -separate {{path/to/rgb.vrt}} {{path/to/red.tif}} {{path/to/green.tif}} {{path/to/blue.tif}}`

- Faceți un mozaic virtual cu culoare de fundal albastru (RGB: 0 255):

`gdalbuildvrt -hidenodata -vrtnodata "{{0 0 255}}" {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`
