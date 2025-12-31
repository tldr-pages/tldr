# pamdice

> Netpbm 이미지를 수직 또는 수평으로 자르기.
> 같이 보기: `pamundice`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamdice.html>.

- 결과 타일이 지정된 높이와 너비를 가지도록 Netpbm 이미지 자르기:

`pamdice {{[-o|-outstem]}} {{경로/대상/파일명_스템}} {{[-h|-height]}} {{값}} {{[-w|-width]}} {{값}} {{경로/대상/입력.ppm}}`

- 생성된 조각을 지정된 양만큼 수평 및 수직으로 겹치도록 만들기:

`pamdice {{[-o|-outstem]}} {{경로/대상/파일명_스템}} {{[-h|-height]}} {{값}} {{[-w|-width]}} {{값}} {{[-ho|-hoverlap]}} {{값}} {{[-vo|-voverlap]}} {{값}} {{경로/대상/입력.ppm}}`
