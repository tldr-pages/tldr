# pnmtorast

> PNM 파일을 Sun 래스터 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtorast.html>.

- PNM 이미지를 RAST 이미지로 변환:

`pnmtorast {{경로/대상/입력.pnm}} > {{경로/대상/출력.rast}}`

- 출력 형식을 `RT_STANDARD` 또는 `RT_BYTE_ENCODED` 형식으로 강제 지정:

`pnmtorast -{{standard|rle}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.rast}}`
