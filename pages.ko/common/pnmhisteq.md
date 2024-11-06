# pnmhisteq

> PNM 이미지의 히스토그램을 균등화.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

- 히스토그램 균등화를 사용하여 PNM 이미지의 대비 증가:

`pnmhisteq {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 회색 픽셀만 수정:

`pnmhisteq -grey {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 히스토그램 균등화에서 검정 또는 흰색 픽셀 제외:

`pnmhisteq -no{{black|white}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
