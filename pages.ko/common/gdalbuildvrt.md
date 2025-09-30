# gdalbuildvrt

> 기존 데이터세트 목록에서 가상 데이터 세트를 구축.
> 더 많은 정보: <https://gdal.org/programs/gdalbuildvrt.html>.

- 디렉토리에 포함된 모든 TIFF 파일로 가상 모자이크를 생성:

`gdalbuildvrt {{경로/대상/출력.vrt}} {{경로/대상/입력_디렉토리/*.tif}}`

- 텍스트 파일에 이름이 지정된 파일로 가상 모자이크를 만듬 :

`gdalbuildvrt -input_file_list {{경로/대상/목록.txt}} {{경로/대상/출력.vrt}}`

- 3개의 단일 대역 입력 파일에서 RGB 가상 모자이크를 만듬:

`gdalbuildvrt -separate {{경로/대상/rgb.vrt}} {{경로/대상/빨강.tif}} {{경로/대상/초록.tif}} {{경로/대상/파랑.tif}}`

- 파란색 배경색 (RGB: 0 0 255)으로 가상 모자이크 만들기:

`gdalbuildvrt -hidenodata -vrtnodata "{{0 0 255}}" {{경로/대상/출력.vrt}} {{경로/대상/입력_디렉토리/*.tif}}`
