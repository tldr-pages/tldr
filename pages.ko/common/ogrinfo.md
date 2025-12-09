# ogrinfo

> OGR 지원 데이터 소스에 대한 정보를 나열합니다.
> 더 많은 정보: <https://gdal.org/programs/ogrinfo.html>.

- 지원되는 형식 나열:

`ogrinfo --formats`

- 데이터 소스의 레이어 나열:

`ogrinfo {{경로/대상/입력.gpkg}}`

- 데이터 소스의 특정 레이어에 대한 자세한 정보 얻기:

`ogrinfo {{경로/대상/입력.gpkg}} {{레이어_이름}}`

- 데이터 소스의 특정 레이어에 대한 요약 정보 표시:

`ogrinfo -so {{경로/대상/입력.gpkg}} {{레이어_이름}}`

- 데이터 소스의 모든 레이어 요약 정보 표시:

`ogrinfo -so -al {{경로/대상/입력.gpkg}}`

- 조건에 맞는 피처의 자세한 정보 표시:

`ogrinfo -where '{{속성_이름 > 42}}' {{경로/대상/입력.gpkg}} {{레이어_이름}}`

- SQL을 사용하여 데이터 소스의 레이어 업데이트:

`ogrinfo {{경로/대상/입력.geojson}} -dialect SQLite -sql "{{UPDATE input SET attribute_name = 'foo'}}"`
