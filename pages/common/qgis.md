# qgis

> View, create, and analyze geographic data in a Geographic Information System.
> Supports rasters, vectors, and project files (.qgs, .qgz, .qlr).
> More information: <https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#running-qgis-with-advanced-settings>.

- Launch QGIS:

`qgis`

- Open a specific project file:

`qgis {{[-p|--project]}} {{path/to/project.qgz}}`

- Open one or more raster or vector files directly:

`qgis {{path/to/file1.tif path/to/file2.shp ...}}`

- Hide the splash screen on startup:

`qgis {{[-n|--nologo]}}`

- Set the initial map extent:

`qgis {{[-e|--extent]}} {{xmin,ymin,xmax,ymax}}`

- Run a Python script on load:

`qgis {{[-f|--code]}} {{path/to/script.py}}`

- Launch QGIS without restoring plugins:

`qgis {{[-P|--noplugins]}}`

- Skip prompts for missing layers when opening a project:

`qgis {{[-B|--skipbadlayers]}} {{[-p|--project]}} {{path/to/project.qgz}}`
