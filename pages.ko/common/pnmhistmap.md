# pnmhistmap

> PNM 이미지의 히스토그램 그리기.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmhistmap.html>.

- PNM 이미지의 히스토그램 그리기:

`pnmhistmap {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 막대 대신 점으로 히스토그램 그리기:

`pnmhistmap -dots {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 포함할 강도 값의 범위 지정:

`pnmhistmap -lval {{최소값}} -rval {{최대값}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
