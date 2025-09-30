# tgatoppm

> TrueVision Targa 파일을 Netpbm 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/tgatoppm.html>.

- TrueVision Targa 파일을 PPM 이미지로 변환:

`tgatoppm {{경로/대상/파일.tga}} > {{경로/대상/출력.ppm}}`

- TGA 헤더의 정보를 `stdout`로 덤프:

`tgatoppm --headerdump {{경로/대상/파일.tga}} > {{경로/대상/출력.ppm}}`

- 입력 이미지의 투명 채널 값을 지정한 파일에 작성:

`tgatoppm --alphaout {{경로/대상/투명도_파일.pgm}} {{경로/대상/파일.tga}} > {{경로/대상/출력.ppm}}`

- 버전 표시:

`tgatoppm -version`
