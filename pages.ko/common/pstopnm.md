# pstopnm

> PostScript 파일을 PNM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pstopnm.html>.

- PS 파일을 PNM 이미지로 변환하고 입력의 페이지 N을 `path/to/fileN.ppm`에 저장:

`pstopnm {{경로/대상/파일.ps}}`

- 출력 형식 명시적으로 지정:

`pstopnm -{{pbm|pgm|ppm}} {{경로/대상/파일.ps}}`

- 출력 해상도를 인치당 도트로 지정:

`pstopnm -dpi {{n}} {{경로/대상/파일.ps}}`
