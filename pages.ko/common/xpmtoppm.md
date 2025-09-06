# xpmtoppm

> X11 픽스맵을 PPM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/xpmtoppm.html>.

- XPM 이미지를 PPM 이미지로 변환:

`xpmtoppm {{경로/대상/입력_파일.xpm}} > {{경로/대상/출력_파일.ppm}}`

- 입력 이미지의 투명 마스크를 지정된 파일에 저장:

`xpmtoppm --alphaout {{경로/대상/알파_파일.pbm}} {{경로/대상/입력_파일.xpm}} > {{경로/대상/출력_파일.ppm}}`
