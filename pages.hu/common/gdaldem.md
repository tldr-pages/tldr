# gdaldem

> Eszköz a digitális domborzati modellek (DEM) elemzésére és megjelenítésére. További információ: <https://gdal.org/programs/gdaldem>.

- Egy DEM dombárnyékának kiszámítása:

`gdaldem hillshade {{path/to/input.tif}} {{path/to/output.tif}}`

- Egy DEM lejtésének kiszámítása:

`gdaldem slope {{path/to/input.tif}} {{path/to/output.tif}}`

- Egy DEM oldalának kiszámítása:

`gdaldem aspect {{path/to/input.tif}} {{path/to/output.tif}}`
