# gdalinfo

> A GDAL által támogatott raszteres adatkészletre vonatkozó különböző információk listázása. További információ: <https://gdal.org/programs/gdalinfo.html>.

- Az összes támogatott raszterformátum felsorolása:

`gdalinfo --formats`

- Egy adott raszteres adatkészletre vonatkozó információk listázása:

`gdalinfo {{path/to/input.tif}}`

- Egy adott raszteradatkészletre vonatkozó információk listázása JSON formátumban:

`gdalinfo -json {{path/to/input.tif}}`

- Egy adott raszteradatkészlet hisztogramértékeinek megjelenítése:

`gdalinfo -hist {{path/to/input.tif}}`

- Információk listázása egy webes térképszolgáltatásról (WMS):

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}}`

- A webes térképszolgáltatás (WMS) egy adott adatkészletére vonatkozó információk listázása:

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}} -sd {{4}}`
