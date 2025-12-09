# ppmlabel

> PPM 이미지에 텍스트 추가.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmlabel.html>.

- 지정된 위치에 PPM 이미지에 텍스트 추가:

`ppmlabel -x {{위치_x}} -y {{위치_y}} -text {{텍스트}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 서로 다른 위치에 여러 텍스트 추가:

`ppmlabel -x {{위치_x1}} -y {{위치_y1}} -text {{텍스트1}} -x {{위치_x2}} -y {{위치_y2}} -text {{텍스트2}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 추가된 텍스트의 선 색상, 배경 색상, 기울기 및 크기 지정:

`ppmlabel -x {{위치_x}} -y {{위치_y}} -color {{선_색상}} -background {{배경_색상}} -angle {{기울기}} -size {{크기}} -text {{텍스트}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`
