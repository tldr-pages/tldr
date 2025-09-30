# rawtoppm

> Raw RGB 스트림을 PPM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/rawtoppm.html>.

- Raw RGB 스트림을 PPM 이미지로 변환:

`rawtoppm {{너비}} {{높이}} {{경로/대상/이미지.raw}} > {{경로/대상/출력.ppm}}`

- 픽셀이 위에서부터가 아닌 아래에서부터 오는 Raw RGB 스트림을 PPM 이미지로 변환:

`rawtoppm {{너비}} {{높이}} {{경로/대상/이미지.raw}} | pamflip -tb > {{경로/대상/출력.ppm}}`

- 지정된 파일의 처음 n 바이트 무시:

`rawtoppm {{너비}} {{높이}} -headerskip {{n}} {{경로/대상/이미지.raw}} > {{경로/대상/출력.ppm}}`

- 지정된 파일의 각 행에서 마지막 m 바이트 무시:

`rawtoppm {{너비}} {{높이}} -rowskip {{m}} {{경로/대상/이미지.raw}} > {{경로/대상/출력.ppm}}`

- 각 픽셀의 색상 구성 요소 순서 지정:

`rawtoppm {{너비}} {{높이}} -{{rgb|rbg|grb|gbr|brg|bgr}} {{경로/대상/이미지.raw}} > {{경로/대상/출력.ppm}}`
