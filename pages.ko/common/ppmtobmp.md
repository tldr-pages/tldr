# ppmtobmp

> PPM 이미지를 BMP 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

- PPM 이미지를 BMP 파일로 변환:

`ppmtobmp {{경로/대상/파일.ppm}} > {{경로/대상/파일.bmp}}`

- Windows BMP 파일 또는 OS/2 BMP 파일을 생성할지 여부를 명시적으로 지정:

`ppmtobmp -{{windows|os2}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.bmp}}`

- 각 픽셀에 사용할 비트 수를 지정:

`ppmtobmp -bbp {{1|4|8|24}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.bmp}}`
