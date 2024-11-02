# pnmshear

> PNM 이미지를 전단 변형.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmshear.html>.

- 지정된 각도로 PNM 이미지 전단 변형:

`pnmshear {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 전단 변형된 이미지의 배경색 지정:

`pnmshear -background {{blue}} {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 안티앨리어싱 없이 수행:

`pnmshear -noantialias {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
