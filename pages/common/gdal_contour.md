# gdal_contour

> Create contour lines and polygons from a digital elevation model.
> More information: <https://gdal.org/programs/gdal_contour.html>.

- Create a vector dataset with contour lines every 100 meter and name the elevation property "ele".

`gdal_contour -a {{ele}} -i {{100.0}} {{input.tif}} {{output.gpkg}}`


- Create a vector dataset with polygons every 100 meter.

`gdal_contour -i {{100.0}} -p {{input.tif}} {{output.gpkg}}`
