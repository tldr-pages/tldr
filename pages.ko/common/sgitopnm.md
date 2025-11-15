# sgitopnm

> SGI 파일을 PNM 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/sgitopnm.html>.

- SGI 이미지를 PNM 파일로 변환:

`sgitopnm {{경로/대상/입력.sgi}} > {{경로/대상/출력.pnm}}`

- SGI 파일에 대한 정보 표시:

`sgitopnm -verbose {{경로/대상/입력.sgi}} > {{경로/대상/출력.pnm}}`

- SGI 파일의 n 채널 추출:

`sgitopnm -channel {{n}} {{경로/대상/입력.sgi}} > {{경로/대상/출력.pnm}}`
