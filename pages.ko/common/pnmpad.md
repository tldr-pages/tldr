# pnmpad

> PNM 이미지에 테두리를 추가.
> 관련 항목: `pnmmargin`, `pamcut`, `pamcomp`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmpad.html>.

- 이미지에 지정된 크기의 테두리 추가:

`pnmpad {{[-l|-left]}} {{100}} {{[-ri|-right]}} {{150}} {{[-t|-top]}} {{123}} {{[-bo|-bottom]}} {{456}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 이미지를 지정된 크기로 패딩:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-he|-height]}} {{500}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 이미지의 너비를 지정된 크기로 패딩하고, 좌우 패딩 비율 조정:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-ha|-halign]}} {{0.7}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 지정된 색상을 사용하여 이미지의 너비를 패딩:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-c|-color]}} {{red}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`
