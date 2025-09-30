# pnmscalefixed

> PNM 파일을 빠르게 확장하되 품질이 다소 저하될 수 있습니다.
> 같이 보기: `pamscale`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmscalefixed.html>.

- 결과가 지정된 크기를 갖도록 이미지를 확장:

`pnmscalefixed -width {{너비}} -height {{높이}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 결과가 지정된 너비를 갖도록 이미지를 확장하며, 가로세로 비율 유지:

`pnmscalefixed -width {{너비}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 이미지의 너비와 높이를 지정된 비율로 변경하여 확장:

`pnmscalefixed -xscale {{x_비율}} -yscale {{y_비율}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
