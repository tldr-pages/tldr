# gdalwarp

> Képreprojekciós és warping segédprogram. További információ: <https://gdal.org/programs/gdalwarp>.

- Raszteres adatkészlet reprojekciója:

`gdalwarp -t_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Raszteres adatkészlet vágása meghatározott koordináták segítségével:

`gdalwarp -te {{min_x}} {{min_y}} {{max_x}} {{max_y}} -te_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Raszteres adatkészlet vágása vektoros réteg használatával:

`gdalwarp -cutline {{path/to/area_to_cut.geojson}} -crop_to_cutline {{path/to/input.tif}} {{path/to/output.tif}}`
