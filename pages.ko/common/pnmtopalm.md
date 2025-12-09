# pnmtopalm

> PNM 이미지를 Palm 비트맵으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtopalm.html>.

- PNM 이미지를 Palm 비트맵으로 변환:

`pnmtopalm {{경로/대상/파일.pnm}} > {{경로/대상/파일.palm}}`

- 결과 비트맵의 색상 깊이 지정:

`pnmtopalm -depth {{1|2|4|8|16}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.palm}}`

- 결과 비트맵에 대한 압축 방법 선택:

`pnmtopalm -{{scanline_compression|rle_compression|packbits_compression}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.palm}}`

- 사용자 지정 색상 맵을 생성하고 결과 비트맵에 포함:

`pnmtopalm -colormap {{경로/대상/파일.pnm}} > {{경로/대상/파일.palm}}`

- 비트맵의 밀도 지정:

`pnmtopalm -density {{72|108|144|216|288}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.palm}}`
