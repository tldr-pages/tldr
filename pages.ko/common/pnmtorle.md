# pnmtorle

> PNM 파일을 Utah Raster Tools RLE 이미지 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtorle.html>.

- PNM 이미지를 RLE 이미지로 변환:

`pnmtorle {{경로/대상/입력.pnm}} > {{경로/대상/출력.rle}}`

- PNM 헤더 정보를 `stdout`에 출력:

`pnmtorle -verbose {{경로/대상/입력.pnm}} > {{경로/대상/출력.rle}}`

- 출력 이미지에 투명 채널 포함, 모든 검은색 픽셀은 완전히 투명하게, 다른 모든 픽셀은 완전히 불투명하게 설정:

`pnmtorle -alpha {{경로/대상/입력.pnm}} > {{경로/대상/출력.rle}}`
