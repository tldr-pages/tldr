# sldtoppm

> AutoCAD 슬라이드 파일을 PPM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/sldtoppm.html>.

- SLD 파일을 PPM 이미지로 변환:

`sldtoppm {{경로/대상/입력.sld}} > {{경로/대상/출력.ppm}}`

- 비정사각 픽셀을 보정하여 이미지의 너비를 조정:

`sldtoppm -adjust {{경로/대상/입력.sld}} > {{경로/대상/출력.ppm}}`
