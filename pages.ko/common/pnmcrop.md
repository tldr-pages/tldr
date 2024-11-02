# pnmcrop

> PNM 이미지 자르기.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmcrop.html>.

- PNM 이미지의 흰색 테두리 제거:

`pnmcrop -white {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 이미지의 상단 및 왼쪽의 지정된 색상의 테두리 제거:

`pnmcrop -bg-color {{색상}} -top -left {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 지정된 모서리의 픽셀 색상을 기준으로 제거할 테두리의 색상 결정:

`pnmcrop -bg-corner {{topleft|topright|bottomleft|bottomright}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- `n` 픽셀 너비의 테두리를 남깁니다. 추가로, 이미지가 전부 배경색으로 이루어져 있을 때의 동작 지정:

`pnmcrop -margins {{n}} -blank-image {{pass|minimize|maxcrop}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`
