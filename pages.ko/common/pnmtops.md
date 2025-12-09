# pnmtops

> PNM 이미지를 PostScript 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtops.html>.

- PNM 이미지를 PS 파일로 변환:

`pnmtops {{경로/대상/파일.pnm}} > {{경로/대상/파일.ps}}`

- 출력 이미지의 크기를 인치 단위로 지정:

`pnmtops -imagewidth {{이미지_너비}} -imageheight {{이미지_높이}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.ps}}`

- 출력 이미지가 위치할 페이지의 크기를 인치 단위로 지정:

`pnmtops -width {{페이지_너비}} -height {{페이지_높이}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.ps}}`
