# qgis

> 지리 정보 시스템에서 지리 데이터를 조회, 생성 및 분석.
> 래스터, 벡터, 프로젝트 파일 (`.qgs`, `.qgz`, `.qlr`)을 지원.
> 더 많은 정보: <https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#running-qgis-with-advanced-settings>.

- QGIS 실행:

`qgis`

- 지정한 프로젝트 파일 열기:

`qgis {{[-p|--project]}} {{경로/대상/프로젝트.qgz}}`

- 하나 이상의 래스터 또는 벡터 파일 직접 열기:

`qgis {{경로/대상/파일1.tif 경로/대상/파일2.shp ...}}`

- 시작 시 스플래시 화면 숨기기:

`qgis {{[-n|--nologo]}}`

- 초기 지도 영역 설정:

`qgis {{[-e|--extent]}} {{xmin,ymin,xmax,ymax}}`

- 시작 시 Python 스크립트 실행:

`qgis {{[-f|--code]}} {{경로/대상/스크립트.py}}`

- 플러그인을 복원하지 않고 QGIS 실행:

`qgis {{[-P|--noplugins]}}`

- 프로젝트를 열 때 누락된 레이어에 대한 확인 메시지 건너뛰기:

`qgis {{[-B|--skipbadlayers]}} {{[-p|--project]}} {{경로/대상/프로젝트.qgz}}`
