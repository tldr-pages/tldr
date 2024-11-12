# pbmclean

> PBM 이미지를 정리하여 고립된 검은색 및 흰색 픽셀을 제거합니다.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmclean.html>.

- 고립된 검은색 및 흰색 픽셀을 제거하여 PBM 이미지 정리:

`pbmclean {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`

- 검은색/흰색 픽셀만 정리:

`pbmclean -{{black|white}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`

- 고립되지 않은 픽셀로 간주되기 위한 최소한의 동일 색상 이웃 픽셀 수 지정:

`pbmclean -minneighbours {{3}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`
