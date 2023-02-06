# gdal2tiles.py

> TMS vagy XYZ csempék generálása egy raszteres adatkészlethez. További információ: <https://gdal.org/programs/gdal2tiles.html>.

- TMS csempék generálása egy raszteres adatkészlet 2-5. zoomolási szintjéhez:

`gdal2tiles.py --zoom={{2-5}} {{path/to/input.tif}} {{path/to/output_directory}}`

- XYZ csempék generálása a raszteres adatkészlet 2-5. nagyítási szintjéhez:

`gdal2tiles.py --zoom={{2-5}} --xyz {{path/to/input.tif}} {{path/to/output_directory}}`
