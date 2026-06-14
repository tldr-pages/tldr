# datashader_cli

> Խոշոր տվյալների հավաքածուների արագ վիզուալացում՝ օգտագործելով CLI՝ տվյալների շեյդերի վրա հիմնված:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wybert/datashader-cli>:.

- Ստեղծեք կետերի ստվերավորված ցրված հողամաս և պահեք այն PNG ֆայլում և սահմանեք ֆոնի գույնը.:

`datashader_cli points {{path/to/input.parquet}} --x {{pickup_x}} --y {{pickup_y}} {{path/to/output.png}} --background {{black|white|#rrggbb}}`

- Պատկերացրեք աշխարհատարածական տվյալները (աջակցում է Geoparquet, shapefile, geojson, geopackage և այլն):

`datashader_cli points {{path/to/input_data.geo.parquet}} {{path/to/output_data.png}} --geo true`

- Օգտագործեք matplotlib պատկերը ցուցադրելու համար.:

`datashader_cli points {{path/to/input_data.geo.parquet}} {{path/to/output_data.png}} --geo {{true}} --matplotlib true`
