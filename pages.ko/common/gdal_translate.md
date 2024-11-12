# gdal_translate

> 래스터 데이터를 다양한 형식으로 변환.
> 더 많은 정보: <https://gdal.org/programs/gdal_translate.html>.

- 래스터 데이터세트를 JPEG 형식으로 변환:

`gdal_translate -of {{JPEG}} {{경로/대상/입력.tif}} {{경로/대상/출력.jpeg}}`

- 레스터 데이터세트에 투영을 할당:

`gdal_translate -a_srs {{EPSG:4326}} {{경로/대상/입력.tif}} {{경로/대상/출력.tif}}`

- 래스터 데이터세트의 크기를 특정 부분으로 줄임:

`gdal_translate -outsize {{40%}} {{40%}} {{경로/대상/입력.tif}} {{경로/대상/출력.tif}}`

- GeoTiff를 클라우드 최적화 GeoTiff로 변환:

`gdal_translate {{경로/대상/입력.tif}} {{경로/대상/출력.tif}} -of COG -co COMPRESS=LZW`
