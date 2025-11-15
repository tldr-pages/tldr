# ppmtoicr

> PPM 이미지를 NCSA ICR 형식으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoicr.html>.

- PPM 이미지를 ICR 파일로 변환:

`ppmtoicr {{경로/대상/파일.ppm}} > {{경로/대상/파일.icr}}`

- 출력 이름을 지정하여 표시:

`ppmtoicr -windowname {{이름}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.icr}}`

- 지정한 배율로 이미지 확대:

`ppmtoicr -expand {{배율}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.icr}}`

- 지정한 번호로 화면에 출력 표시:

`ppmtoicr -display {{번호}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.icr}}`
