# gdalinfo

> GDAL 지원 래스터 데이터세트에 대한 다양한 정보를 나열.
> 더 많은 정보: <https://gdal.org/programs/gdalinfo.html>.

- 지원하는 래스터 포맷 나열:

`gdalinfo --formats`

- 특정 래스터 데이터세트에 대한 정보 나열:

`gdalinfo {{경로/대상/입력.tif}}`

- 특정 래스터 데이터세트에 대한 정보를 JSON 형식으로 나열:

`gdalinfo -json {{경로/대상/입력.tif}}`

- 특정 래스터 데이터세트의 히스토그램 값 표시:

`gdalinfo -hist {{경로/대상/입력.tif}}`

- 웹 맵 서비스(WMS)에 대한 정보를 나열:

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}}`

- 웹 맵 서비스(WMS)의 특정 데이터세트에 대한 정보를 나열:

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}} -sd {{4}}`
