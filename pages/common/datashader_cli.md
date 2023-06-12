# datashader_cli

> Quick visualization of large datasets using CLI based on [datashader](https://github.com/holoviz/datashader).
> More information: <https://github.com/wybert/datashader-cli>.


- Create a shaded scatter plot of points and save it to png file, set background color to black.
    
`datashader_cli points nyc_taxi.parquet --x pickup_x --y pickup_y pickup-scatter.png --background black`

- Visualize the geospaital data, support Geoparquet, shapefile, geojson, geopackage, etc.

`datashader_cli points data.geo.parquet data.png --geo true`

- Use matplotlib to render the image

`datashader_cli points data.geo.parquet data.png --geo true --matplotlib true`
    
