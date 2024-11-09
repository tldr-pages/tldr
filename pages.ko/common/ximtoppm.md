# ximtoppm

> XIM 파일을 PPM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ximtoppm.html>.

- XIM 이미지를 PPM 이미지로 변환:

`ximtoppm {{경로/대상/입력_파일.xim}} > {{경로/대상/출력_파일.ppm}}`

- 입력 이미지의 투명 마스크를 지정된 파일에 저장:

`ximtoppm --alphaout {{경로/대상/알파_파일.pbm}} {{경로/대상/입력_파일.xim}} > {{경로/대상/출력_파일.ppm}}`
