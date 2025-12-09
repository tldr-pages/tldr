# ppmntsc

> PPM 이미지의 RGB 색상을 NTSC 또는 PAL 컬러 시스템과 호환되도록 만듭니다.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmntsc.html>.

- PPM 이미지의 RGB 색상을 NTSC 컬러 시스템과 호환되도록 만들기:

`ppmntsc {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- PPM 이미지의 RGB 색상을 PAL 컬러 시스템과 호환되도록 만들기:

`ppmntsc --pal {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 입력 이미지의 불법 픽셀 수를 `stderr`에 출력:

`ppmntsc --verbose {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 합법/불법/수정된 픽셀만 출력하고 다른 픽셀은 검정색으로 설정:

`ppmntsc --{{legalonly|illegalonly|correctedonly}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`
