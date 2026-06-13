# pdftocairo

> PDF 파일을 PNG/JPEG/TIFF/PDF/PS/EPS/SVG 형식으로 변환하는 도구입니다 (cairo 사용).
> 더 많은 정보: <https://manned.org/pdftocairo>.

- PDF 파일을 JPEG로 변환:

`pdftocairo {{경로/대상/파일.pdf}} -jpeg`

- 출력물이 용지를 채우도록 확장하여 PDF로 변환:

`pdftocairo {{경로/대상/파일.pdf}} {{출력.pdf}} -pdf -expand`

- 변환할 첫 페이지와 마지막 페이지를 지정하여 SVG로 변환:

`pdftocairo {{경로/대상/파일.pdf}} {{출력.svg}} -svg -f {{첫_페이지}} -l {{마지막_페이지}}`

- 200ppi 해상도로 PNG로 변환:

`pdftocairo {{경로/대상/파일.pdf}} {{출력.png}} -png -r 200`

- A3 용지 크기로 설정하여 그레이스케일 TIFF로 변환:

`pdftocairo {{경로/대상/파일.pdf}} -tiff -gray -paper A3`

- 좌측 상단 모서리에서 x와 y 픽셀을 잘라내어 PNG로 변환:

`pdftocairo {{경로/대상/파일.pdf}} -png -x {{x_픽셀}} -y {{y_픽셀}}`
