# pnmtotiffcmyk

> PNM 이미지를 CMYK로 인코딩된 TIFF로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>.

- PNM 이미지를 CMYK로 인코딩된 TIFF로 변환:

`pnmtotiffcmyk {{경로/대상/입력_파일.pnm}} > {{경로/대상/출력_파일.tiff}}`

- TIFF 압축 방식 지정:

`pnmtotiffcmyk -{{none|packbits|lzw}} {{경로/대상/입력_파일.pnm}} > {{경로/대상/출력_파일.tiff}}`

- 채우기 순서 제어:

`pnmtotiffcmyk -{{msb2lsb|lsb2msb}} {{경로/대상/입력_파일.pnm}} > {{경로/대상/출력_파일.tiff}}`
