# gdalwarp

> Image reprojection and warping utility.
> More information: <https://gdal.org/programs/gdalwarp.html>.

- Reproject a raster dataset:

`gdalwarp -t_srs {{EPSG:4326}} {{input.tif}} {{output.tif}}`

- Crop a raster dataset by coordinates:

`gdalwarp -te {{min_x}} {{min_y}} {{max_x}} {{max_y}} -te_srs {{EPSG:4326}} {{input.tif}} {{output.tif}}`

- Crop a raster dataset by a vector layer:

`gdalwarp -cutline {{aoi.geojson}} -crop_to_cutline {{world.tif}} {{out.tif}}`

- Crop a raster datasets by features of a vector layer:

`gdalwarp -cutline {{countries.shp}} -cwhere {{"NAME IN ('Germany', 'France')"}} -crop_to_cutline {{input.tif}} {{many_countries.tif}}`
