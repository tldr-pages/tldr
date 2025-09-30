# jpegtran

> JPEG 파일의 무손실 변환 수행.
> 더 많은 정보: <https://manned.org/jpegtran>.

- 이미지를 수평 또는 수직으로 반전:

`jpegtran -flip {{horizontal|vertical}} {{경로/대상/이미지.jpg}} > {{경로/대상/출력.jpg}}`

- 이미지를 시계 방향으로 90, 180 또는 270도 회전:

`jpegtran -rotate {{90|180|270}} {{경로/대상/이미지.jpg}} > {{경로/대상/출력.jpg}}`

- 이미지의 좌상단에서 우하단 축으로 대칭 변환:

`jpegtran -transpose {{경로/대상/이미지.jpg}} > {{경로/대상/출력.jpg}}`

- 이미지의 우상단에서 좌하단 축으로 대칭 변환:

`jpegtran -transverse {{경로/대상/이미지.jpg}} > {{경로/대상/출력.jpg}}`

- 이미지를 그레이스케일로 변환:

`jpegtran -grayscale {{경로/대상/이미지.jpg}} > {{경로/대상/출력.jpg}}`

- 이미지의 좌상단에서 너비 `W`와 높이 `H`의 직사각형 영역으로 자르고, 특정 파일에 출력 저장:

`jpegtran -crop {{W}}x{{H}} -outfile {{경로/대상/출력.jpg}} {{경로/대상/이미지.jpg}}`

- 이미지의 좌상단에서 시작점 `X`와 `Y`로부터 너비 `W`와 높이 `H`의 직사각형 영역으로 자르기:

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{경로/대상/이미지.jpg}} > {{경로/대상/출력.jpg}}`
