# gdalwarp

> 이미지 재투영 및 워핑 유틸리티.
> 더 많은 정보: <https://gdal.org/programs/gdalwarp.html>.

- 래스터 데이터세트 재투영:

`gdalwarp -t_srs {{EPSG:4326}} {{경로/대상/입력.tif}} {{경로/대상/출력.tif}}`

- 특정 좌표를 사용하여 래스터 데이터세트 자르기:

`gdalwarp -te {{min_x}} {{min_y}} {{max_x}} {{max_y}} -te_srs {{EPSG:4326}} {{경로/대상/입력.tif}} {{경로/대상/출력.tif}}`

- 벡터 레이어를 사용하여 래스터 데이터세트 자르기:

`gdalwarp -cutline {{경로/대상/자르기_위한_영역.geojson}} -crop_to_cutline {{경로/대상/입력.tif}} {{경로/대상/출력.tif}}`
