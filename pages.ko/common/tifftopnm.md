# tifftopnm

> TIFF 이미지를 PNM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/tifftopnm.html>.

- TIFF를 PNM 파일로 변환:

`tifftopnm {{경로/대상/입력_파일.tiff}} > {{경로/대상/출력_파일.pnm}}`

- 입력 이미지의 알파 채널을 포함하는 PGM 파일 생성:

`tifftopnm -alphaout {{경로/대상/알파_파일.pgm}} {{경로/대상/입력_파일.tiff}} > {{경로/대상/출력_파일.pnm}}`

- 입력 TIFF 이미지의 `fillorder` 태그 고려:

`tifftopnm -respectfillorder {{경로/대상/입력_파일.tiff}} > {{경로/대상/출력_파일.pnm}}`

- TIFF 헤더 정보를 `stderr`에 출력:

`tifftopnm -headerdump {{경로/대상/입력_파일.tiff}} > {{경로/대상/출력_파일.pnm}}`
