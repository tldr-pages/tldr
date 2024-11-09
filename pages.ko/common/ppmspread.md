# ppmspread

> PPM 이미지의 픽셀을 무작위로 변위.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmspread.html>.

- PPM 이미지의 픽셀을 최대 {{a}}만큼 무작위로 변위:

`ppmspread {{a}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 의사 난수 생성기에 시드 지정:

`ppmspread {{a}} {{경로/대상/입력_파일.ppm}} -randomseed {{시드}} > {{경로/대상/출력_파일.ppm}}`
