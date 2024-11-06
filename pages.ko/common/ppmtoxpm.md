# ppmtoxpm

> PPM 이미지를 X11 버전 3 픽스맵으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoxpm.html>.

- PPM 이미지를 XPM 이미지로 변환:

`ppmtoxpm {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.xpm}}`

- 출력 XPM 이미지에서 접두사 문자열 지정:

`ppmtoxpm -name {{접두사_문자열}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.xpm}}`

- 출력 XPM 파일에서 색상을 이름 대신 16진수 코드로 지정:

`ppmtoxpm -hexonly {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.xpm}}`

- 지정된 PGM 파일을 투명 마스크로 사용:

`ppmtoxpm -alphamask {{경로/대상/알파_파일.pgm}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.xpm}}`
