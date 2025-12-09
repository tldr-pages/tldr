# palmtopnm

> Palm 비트맵 파일을 PNM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Palm 비트맵을 PNM 이미지로 변환:

`palmtopnm {{경로/대상/파일.palm}} > {{경로/대상/파일.pnm}}`

- 입력 파일에 대한 정보 표시:

`palmtopnm -verbose {{경로/대상/파일.palm}} > {{경로/대상/파일.pnm}}`

- 입력 파일에 포함된 이미지의 n번째 렌디션 변환:

`palmtopnm -rendition {{n}} {{경로/대상/파일.palm}} > {{경로/대상/파일.pnm}}`

- 입력 파일의 색상 히스토그램을 `stdout`에 출력:

`palmtopnm -showhist {{경로/대상/파일.palm}} > {{경로/대상/파일.pnm}}`

- 설정된 경우 입력 이미지의 투명 색상 출력:

`palmtopnm -transparent {{경로/대상/파일.palm}}`
