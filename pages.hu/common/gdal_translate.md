# gdal_translate

> Raszteres adatok konvertálása különböző formátumok között. További információ: <https://gdal.org/programs/gdal_translate>.

- Raszteres adatkészlet átalakítása JPEG formátumba:

`gdal_translate -of {{JPEG}} {{path/to/input.tif}} {{path/to/output.jpeg}}`

- Raszteres adatkészlethez vetület hozzárendelése:

`gdal_translate -a_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Raszteres adatkészlet méretének csökkentése egy adott töredékre:

`gdal_translate -outsize {{40%}} {{40%}} {{path/to/input.tif}} {{path/to/output.tif}}`

- GeoTiff-formátum átalakítása felhőoptimalizált GeoTiff-formátummá:

`gdal_translate {{path/to/input.tif}} {{path/to/output.tif}} -of COG -co COMPRESS=LZW`
