# ppmtosixel

> PPM 이미지를 DEC sixel 형식으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtosixel.html>.

- PPM 이미지를 DEC sixel 형식으로 변환:

`ppmtosixel {{경로/대상/파일.ppm}} > {{경로/대상/파일.sixel}}`

- 인쇄 속도가 훨씬 느린 비압축 SIXEL 파일 생성:

`ppmtosixel -raw {{경로/대상/파일.ppm}} > {{경로/대상/파일.sixel}}`

- 왼쪽 여백을 1.5인치 추가:

`ppmtosixel -margin {{경로/대상/파일.ppm}} > {{경로/대상/파일.sixel}}`

- 제어 코드를 보다 이식 가능하게(공간 효율성은 떨어짐) 인코딩:

`ppmtosixel -7bit {{경로/대상/파일.ppm}} > {{경로/대상/파일.sixel}}`
