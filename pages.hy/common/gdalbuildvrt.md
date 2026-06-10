# gdalbuildvrt

> Ստեղծեք վիրտուալ տվյալների հավաքածուներ առկա տվյալների հավաքածուների ցանկից:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/gdalbuildvrt.html>:.

- Գրացուցակում պարունակվող բոլոր TIFF ֆայլերից պատրաստեք վիրտուալ խճանկար.:

`gdalbuildvrt {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`

- Ստեղծեք վիրտուալ խճանկար ֆայլերից, որոնց անունը նշված է տեքստային ֆայլում.:

`gdalbuildvrt -input_file_list {{path/to/list.txt}} {{path/to/output.vrt}}`

- Ստեղծեք RGB վիրտուալ խճանկար 3 միաշերտ մուտքային ֆայլերից.:

`gdalbuildvrt -separate {{path/to/rgb.vrt}} {{path/to/red.tif}} {{path/to/green.tif}} {{path/to/blue.tif}}`

- Կատարեք վիրտուալ խճանկար կապույտ ֆոնի գույնով (RGB: 0 0 255):

`gdalbuildvrt -hidenodata -vrtnodata "{{0 0 255}}" {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`
