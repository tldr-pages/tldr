# pcxtoppm

> PCX 파일을 PPM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pcxtoppm.html>.

- PCX 파일을 PPM 이미지로 변환:

`pcxtoppm {{경로/대상/파일.pcx}} > {{경로/대상/파일.ppm}}`

- PCX 파일이 팔레트를 제공하더라도 미리 정의된 표준 팔레트를 사용:

`pcxtoppm -stdpalette {{경로/대상/파일.pcx}} > {{경로/대상/파일.ppm}}`

- PCX 헤더 정보를 `stdout`에 출력:

`pcxtoppm -verbose {{경로/대상/파일.pcx}} > {{경로/대상/파일.ppm}}`
