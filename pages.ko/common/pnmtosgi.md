# pnmtosgi

> PNM 파일을 SGI 이미지 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

- PNM 이미지를 SGI 이미지로 변환:

`pnmtosgi {{경로/대상/입력.pnm}} > {{경로/대상/출력.sgi}}`

- 압축을 비활성화하거나 활성화:

`pnmtosgi -{{verbatim|rle}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.sgi}}`

- SGI 이미지 헤더의 `imagename` 필드에 지정된 문자열을 기록:

`pnmtosgi -imagename {{문자열}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.sgi}}`
