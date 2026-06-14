# gdal2tiles.py

> Ստեղծեք TMS կամ XYZ սալիկներ ռաստերային տվյալների բազայի համար:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/gdal2tiles.html>:.

- Ստեղծեք TMS սալիկներ ռաստերային տվյալների մեծացման 2-ից 5 մակարդակների համար.:

`gdal2tiles.py --zoom 2-5 {{path/to/input.tif}} {{path/to/output_directory}}`

- Ստեղծեք XYZ սալիկներ ռաստերային տվյալների մեծացման 2-ից 5 մակարդակների համար.:

`gdal2tiles.py --zoom 2-5 --xyz {{path/to/input.tif}} {{path/to/output_directory}}`
