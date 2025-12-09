# pnmnorm

> PNM 이미지의 대비를 정규화합니다.
> 같이 보기: `pnmhisteq`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- 가장 밝은 픽셀을 흰색으로, 가장 어두운 픽셀을 검은색으로 설정하고 그 사이의 픽셀을 선형적으로 분포시키기:

`pnmnorm {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 가장 밝은 픽셀을 흰색으로, 가장 어두운 픽셀을 검은색으로 설정하고 그 사이의 픽셀을 n의 밝기로 50% 밝게 되도록 이차적으로 분포시키기:

`pnmnorm -midvalue {{n}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 픽셀의 색조는 유지하고 밝기만 수정하기:

`pnmnorm -keephues {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 픽셀의 밝기를 계산하는 방법 지정하기:

`pnmnorm -{{luminosity|colorvalue|saturation}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`
