# pnmalias

> PNM 이미지에 안티앨리어싱 적용.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmalias.html>.

- PNM 이미지에 안티앨리어싱 적용, 검은 픽셀을 배경으로, 흰 픽셀을 전경으로 처리:

`pnmalias {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 배경색과 전경색을 명시적으로 지정:

`pnmalias -bcolor {{배경_색상}} -fcolor {{전경_색상}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 전경 픽셀에만 안티앨리어싱 적용:

`pnmalias -fonly {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`

- 배경 픽셀 주변의 모든 픽셀에 안티앨리어싱 적용:

`pnmalias -balias {{경로/대상/입력.pnm}} > {{경로/대상/출력.ppm}}`
