# pcdovtoppm

> 사진 CD의 개요 파일을 기반으로 색인 이미지를 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- PCD 개요 파일에서 PPM 색인 이미지 생성:

`pcdovtoppm {{경로/대상/파일.pcd}} > {{경로/대상/출력.ppm}}`

- 출력 이미지의 최대 너비와 출력에 포함된 각 이미지의 최대 크기 지정:

`pcdovtoppm {{[-m|-maxwidth]}} {{너비}} {{[-s|-size]}} {{크기}} {{경로/대상/파일.pcd}} > {{경로/대상/출력.ppm}}`

- 가로로 배치할 이미지의 최대 수와 최대 색상 수 지정:

`pcdovtoppm {{[-a|-across]}} {{이미지_수}} {{[-c|-colors]}} {{색상_수}} {{경로/대상/파일.pcd}} > {{경로/대상/출력.ppm}}`

- 주석에 사용할 폰트를 지정하고 배경을 흰색으로 칠하기:

`pcdovtoppm {{[-f|-font]}} {{폰트}} {{[-w|-white]}} {{경로/대상/파일.pcd}} > {{경로/대상/출력.ppm}}`
