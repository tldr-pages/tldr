# pnmpaste

> PNM 이미지를 다른 PNM 이미지에 붙여 넣기.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmpaste.html>.

- 지정된 좌표에 PNM 이미지를 다른 PNM 이미지에 붙여 넣기:

`pnmpaste {{x}} {{y}} {{경로/대상/이미지1.pnm}} {{경로/대상/이미지2.pnm}} > {{경로/대상/출력.pnm}}`

- `stdin`에서 읽은 이미지를 지정된 이미지에 붙여 넣기:

`{{명령어}} | pnmpaste {{x}} {{y}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 겹치는 픽셀을 지정된 불리언 연산으로 결합하기, 이때 흰색 픽셀은 `true`, 검은색 픽셀은 `false`로 표현:

`pnmpaste -{{and|nand|or|nor|xor|xnor}} {{x}} {{y}} {{경로/대상/이미지1.pnm}} {{경로/대상/이미지2.pnm}} > {{경로/대상/출력.pnm}}`
