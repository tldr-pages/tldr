# qgis

> A free and open source Geographic Information System.
> Supports rasters, vectors, and project files (.qgs, .qgz, .qlr).
> More information: <https://qgis.org>.

- Launch QGIS:

`qgis`

- Open a specific project file:

`qgis --project {{path/to/project.qgz}}`

- Open one or more raster or vector files directly:

`qgis {{path/to/file1.tif}} {{path/to/file2.shp}}`

- Hide the splash screen on startup:

`qgis --nologo`

- Set the initial map extent:

`qgis --extent {{xmin,ymin,xmax,ymax}}`

- Run a Python script on load:

`qgis --code {{path/to/script.py}}`

- Launch QGIS without restoring plugins:

`qgis --noplugins`

- Skip prompts for missing layers when opening a project:

`qgis --skipbadlayers --project {{path/to/project.qgz}}`
