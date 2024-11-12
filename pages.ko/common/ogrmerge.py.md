# ogrmerge.py

> 여러 벡터 데이터셋을 하나로 병합.
> 더 많은 정보: <https://gdal.org/programs/ogrmerge.html>.

- 각 입력 셰이프파일에 대해 레이어가 포함된 GeoPackage 생성:

`ogrmerge.py -f {{GPKG}} -o {{경로/대상/출력.gpkg}} {{경로/대상/입력1.shp 경로/대상/입력2.shp ...}}`

- 각 입력 GeoJSON에 대해 레이어가 포함된 가상 데이터 소스(VRT) 생성:

`ogrmerge.py -f {{VRT}} -o {{경로/대상/출력.vrt}} {{경로/대상/입력1.geojson 경로/대상/입력2.geojson ...}}`

- 두 벡터 데이터셋을 연결하고 속성 'source_name'에 데이터셋의 소스 이름 저장:

`ogrmerge.py -single -f {{GeoJSON}} -o {{경로/대상/출력.geojson}} -src_layer_field_name country {{소스_이름}} {{경로/대상/입력1.shp 경로/대상/입력2.shp ...}}`
