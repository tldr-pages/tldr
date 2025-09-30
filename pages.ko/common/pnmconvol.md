# pnmconvol

> PNM 이미지를 컨볼루션.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmconvol.html>.

- 지정된 컨볼루션 행렬로 PNM 이미지 컨볼루션:

`pnmconvol -matrix=-1,3,-1 {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 입력 이미지의 각 레이어에 대해 파일로 지정된 컨볼루션 행렬로 PNM 이미지 컨볼루션:

`pnmconvol -matrixfile {{경로/대상/행렬1,경로/대상/행렬2,...}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 지정된 PNM 파일의 컨볼루션 행렬로 PNM 이미지 컨볼루션:

`pnmconvol {{경로/대상/행렬.pnm}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 컨볼루션 행렬의 가중치를 합이 1이 되도록 정규화:

`pnmconvol -matrix=-1,3,-1 -normalize {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`
