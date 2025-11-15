# pnmcolormap

> PNM 이미지에 대한 양자화 색상 맵 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- 입력 이미지와 최대한 유사하게 `n_colors` 이하의 색상만 사용하는 이미지 생성:

`pnmcolormap {{n_colors}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 작은 디테일이 있는 이미지에 더 나은 결과를 제공할 수 있는 splitspread 전략 사용:

`pnmcolormap -splitspread {{n_colors}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 색상 맵을 정렬, 색상 맵 비교에 유용:

`pnmcolormap -sort {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`
