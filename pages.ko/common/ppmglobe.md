# ppmglobe

> 이미지를 구에 붙일 수 있는 띠 형태로 변환.
> 관련 항목: `pnmmercator`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmglobe.html>.

- 이미지를 잘라 구에 붙일 수 있는 띠 형태로 변환:

`ppmglobe {{띠_개수}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력파일.ppm}}`

- 띠 사이의 영역에 지정한 색상을 사용하여 변환:

`ppmglobe {{[-b|-background]}} {{red}} {{띠_개수}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력파일.ppm}}`
