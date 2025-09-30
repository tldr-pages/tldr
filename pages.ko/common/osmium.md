# osmium

> OpenStreetMap (OSM) 파일을 처리하는 다목적 도구.
> 더 많은 정보: <https://osmcode.org/osmium-tool/manual>.

- 파일 정보 표시:

`osmium fileinfo {{경로/대상/입력.osm}}`

- 내용 표시:

`osmium show {{경로/대상/입력.osm}}`

- 파일 형식을 PBF에서 XML로 변환:

`osmium cat {{경로/대상/입력.osm.pbf}} -o {{경로/대상/출력.osm}}`

- 주어진 경계 상자에 의해 지리적 영역 추출:

`osmium extract -b {{최소_경도}},{{최소_위도}},{{최대_경도}},{{최대_위도}} {{경로/대상/입력.pbf}} -o {{경로/대상/출력.pbf}}`

- GeoJSON 파일에 의해 지리적 영역 추출:

`osmium extract -p {{경로/대상/다각형.geojson}} {{경로/대상/입력.pbf}} -o {{경로/대상/출력.pbf}}`

- "restaurant"으로 태그된 모든 객체 필터링:

`osmium tags-filter {{경로/대상/입력.pbf}} amenity=restaurant -o {{경로/대상/출력.pbf}}`

- "highway"로 태그된 "way" 객체 필터링:

`osmium tags-filter {{경로/대상/입력.pbf}} w/highway -o {{경로/대상/출력.pbf}}`

- "building"으로 태그된 "way" 및 "relation" 객체 필터링:

`osmium tags-filter {{경로/대상/입력.pbf}} wr/building -o {{경로/대상/출력.pbf}}`
