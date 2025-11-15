# pbmnoise

> 백색 소음을 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmnoise.html>.

- 백색 소음을 포함한 PGM 이미지 생성:

`pbmnoise {{너비}} {{높이}} > {{경로/대상/출력.pbm}}`

- 의사 난수 생성기의 시드 지정:

`pbmnoise {{너비}} {{높이}} -randomseed {{값}} > {{경로/대상/출력.pbm}}`

- 원하는 흰색 대 검은색 픽셀 비율 지정:

`pbmnoise {{너비}} {{높이}} -ratio {{1/3}} > {{경로/대상/출력.pbm}}`
