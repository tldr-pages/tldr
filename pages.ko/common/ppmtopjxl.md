# ppmtopjxl

> PPM 이미지를 HP PaintJet XL PCL 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtopjxl.html>.

- PPM 이미지를 PJXL 파일로 변환:

`ppmtopjxl {{경로/대상/이미지.ppm}} > {{경로/대상/출력파일.pjxl}}`

- 입력 이미지 크기 조정:

`ppmtopjxl {{[-xsi|-xsize]}} {{10cm}} {{[-ysi|-ysize]}} {{5cm}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력파일.pjxl}}`

- 입력 이미지 위치 이동:

`ppmtopjxl {{[-xsh|-xshift]}} {{10pt}} {{[-ysh|-yshift]}} {{5pt}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력파일.pjxl}}`

- 기본 TIFF 4.0 압축 방식을 사용하지 않고 변환:

`ppmtopjxl {{[-n|-nopack]}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력파일.pjxl}}`
