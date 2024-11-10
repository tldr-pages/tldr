# pnmremap

> PNM 이미지의 색상을 교체.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmremap.html>.

- 이미지의 색상을 지정된 색상 팔레트로 교체:

`pnmremap -mapfile {{경로/대상/팔레트_파일.ppm}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 팔레트에 없는 색상을 표현하기 위해 Floyd-Steinberg 디더링 사용:

`pnmremap -mapfile {{경로/대상/팔레트_파일.ppm}} -floyd {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 팔레트의 첫 번째 색상을 사용하여 팔레트에 없는 색상을 표현:

`pnmremap -mapfile {{경로/대상/팔레트_파일.ppm}} -firstisdefault {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 지정된 색상을 사용하여 팔레트에 없는 색상을 표현:

`pnmremap -mapfile {{경로/대상/팔레트_파일.ppm}} -missingcolor {{색상}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
