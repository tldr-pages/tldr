# ppmdist

> PPM 이미지를 그레이스케일 버전으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmdist.html>.

- 지정된 PPM 이미지의 그레이스케일 버전 생성:

`ppmdist {{경로/대상/입력.ppm}} > {{경로/대상/출력.pgm}}`

- 지정된 방법을 사용하여 색상을 그레이 레벨로 매핑:

`ppmdist -{{frequency|intensity}} {{경로/대상/입력.ppm}} > {{경로/대상/출력.pgm}}`
