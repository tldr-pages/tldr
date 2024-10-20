# gdal2tiles.py

> 래스터 데이터세트를 위한 TMS 또는 XYZ 타일을 생성.
> 더 많은 정보: <https://gdal.org/programs/gdal2tiles.html>.

- 래스터 데이터세트의 확대/축소 수준 2~5에 대한 TMS 타일을 생성:

`gdal2tiles.py --zoom 2-5 {{경로/대상/입력파일.tif}} {{경로/대상/출력_디렉토리}}`

- 래스터 데이터세트의 확대/축소 수준 2~5에 대한 XYZ 타일을 생성:

`gdal2tiles.py --zoom 2-5 --xyz {{경로/대상/입력파일.tif}} {{경로/대상/출력_디렉토리}}`
