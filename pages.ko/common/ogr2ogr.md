# ogr2ogr

> 지리공간 벡터 데이터를 파일 형식 간에 변환.
> 더 많은 정보: <https://gdal.org/programs/ogr2ogr.html>.

- 쉐이프파일을 지오패키지로 변환:

`ogr2ogr -f GPKG {{경로/대상/출력.gpkg}} {{경로/대상/입력.shp}}`

- 조건에 맞는 특징만 포함하도록 GeoJSON 축소:

`ogr2ogr -where '{{myProperty > 42}}' -f {{GeoJSON}} {{경로/대상/출력.geojson}} {{경로/대상/입력.geojson}}`

- 지오패키지의 좌표 참조 시스템을 `EPSG:4326`에서 `EPSG:3857`로 변경:

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{경로/대상/출력.gpkg}} {{경로/대상/입력.gpkg}}`

- CSV 파일을 지오패키지로 변환하며 좌표 열의 이름을 지정하고 좌표 참조 시스템 할당:

`ogr2ogr -f GPKG {{경로/대상/출력.gpkg}} {{경로/대상/입력.csv}} -oo X_POSSIBLE_NAMES={{경도}} -oo Y_POSSIBLE_NAMES={{위도}} -a_srs {{EPSG:4326}}`

- 지오패키지를 PostGIS 데이터베이스로 로드:

`ogr2ogr -f PostgreSQL PG:dbname="{{데이터베이스_이름}}" {{경로/대상/입력.gpkg}}`

- 주어진 경계 상자로 지오패키지 파일의 레이어를 자르기:

`ogr2ogr -spat {{최소_x}} {{최소_y}} {{최대_x}} {{최대_y}} -f GPKG {{경로/대상/출력.gpkg}} {{경로/대상/입력.gpkg}}`
