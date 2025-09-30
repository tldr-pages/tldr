# ppmtoacad

> PPM 이미지를 AutoCAD 데이터베이스 또는 슬라이드로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoacad.html>.

- PPM 이미지를 AutoCAD 슬라이드로 변환:

`ppmtoacad {{경로/대상/파일.ppm}} > {{경로/대상/파일.acad}}`

- PPM 이미지를 AutoCAD 바이너리 데이터베이스 가져오기 파일로 변환:

`ppmtoacad -dxb {{경로/대상/파일.ppm}} > {{경로/대상/파일.dxb}}`

- 출력의 색상을 8가지 RGB 음영으로 제한:

`ppmtoacad -8 {{경로/대상/파일.ppm}} > {{경로/대상/파일.dxb}}`
