# pnmcolormap

> PNM 이미지에 대한 양자화 색상 맵 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- 입력 이미지에 최대한 가깝게 `n_colors`개 또는 그 이하의 색상만 사용하여 이미지 생성:

`pnmcolormap {{n_colors}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 작은 세부사항이 있는 이미지의 결과를 개선할 수 있는 splitspread 전략을 사용하여 출력 색상 결정:

`pnmcolormap -splitspread {{n_colors}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 결과 색상 맵을 정렬하여 색상 맵을 비교할 때 유용하게 사용:

`pnmcolormap -sort {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`
