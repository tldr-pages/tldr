# pnmsmooth

> PNM 이미지를 부드럽게 처리.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmsmooth.html>.

- 3x3 크기의 컨볼루션 행렬을 사용하여 PNM 이미지 부드럽게 처리:

`pnmsmooth {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 가로 너비 x 세로 높이 크기의 컨볼루션 행렬을 사용하여 PNM 이미지 부드럽게 처리:

`pnmsmooth -width {{너비}} -height {{높이}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
