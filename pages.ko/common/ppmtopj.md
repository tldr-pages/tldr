# ppmtopj

> PPM 파일을 HP PaintJet 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtopj.html>.

- PPM 파일을 HP PaintJet 파일로 변환:

`ppmtopj {{경로/대상/입력.ppm}} > {{경로/대상/출력.pj}}`

- 이미지를 x 및 y 방향으로 이동:

`ppmtopj -xpos {{dx}} -ypos {{dy}} {{경로/대상/입력.ppm}} > {{경로/대상/출력.pj}}`

- 감마 값을 명시적으로 지정:

`ppmtopj -gamma {{감마}} {{경로/대상/입력.ppm}} > {{경로/대상/출력.pj}}`
