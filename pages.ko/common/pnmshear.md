# pnmshear

> PNM 이미지를 전단(기울이기)합니다.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmshear.html>.

- 지정된 각도로 PNM 이미지 전단:

`pnmshear {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 전단된 이미지의 배경색 지정:

`pnmshear -background {{파랑}} {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 안티앨리어싱 없이 수행:

`pnmshear -noantialias {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
