# gdalwarp

> Պատկերի վերարտադրման և աղավաղման օգտակարություն:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/gdalwarp.html>:.

- Վերանախագծել ռաստերային տվյալների բազա.:

`gdalwarp -t_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Կտրեք ռաստերային հավաքածուն՝ օգտագործելով հատուկ կոորդինատներ.:

`gdalwarp -te {{min_x}} {{min_y}} {{max_x}} {{max_y}} -te_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Կտրեք ռաստերային հավաքածուն՝ օգտագործելով վեկտորային շերտ.:

`gdalwarp -cutline {{path/to/area_to_cut.geojson}} -crop_to_cutline {{path/to/input.tif}} {{path/to/output.tif}}`
