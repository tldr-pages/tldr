# datashader_cli

> Datashader 기반의 CLI을 사용하여 대규모 데이터 세트를 빠르게 시각화.
> 더 많은 정보: <https://github.com/wybert/datashader-cli>.

- 점의 음영처리된 산점도를 생성하고 PNG 파일로 저장한 후 배경색을 설정:

`datashader_cli points {{경로/대상/입력.parquet}} --x {{pickup_x}} --y {{pickup_y}} {{경로/대상/출력.png}} --background {{black|white|#rrggbb}}`

- 지리공간 데이터 시각화 (Geoparquet, shapefile, geojson, geopackage 등 지원):

`datashader_cli points {{경로/대상/입력_데이터.geo.parquet}} {{경로/대상/출력_데이터.png}} --geo true`

- matplotlib를 사용해 이미지 렌더링:

`datashader_cli points {{경로/대상/입력_데이터.geo.parquet}} {{경로/대상/출력_데이터.png}} --geo {{true}} --matplotlib true`
