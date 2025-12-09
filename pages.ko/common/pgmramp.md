# pgmramp

> 그레이스케일 맵 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmramp.html>.

- 좌에서 우로 그레이스케일 맵 생성:

`pgmramp -lr > {{경로/대상/출력.pgm}}`

- 위에서 아래로 그레이스케일 맵 생성:

`pgmramp -tb > {{경로/대상/출력.pgm}}`

- 직사각형 그레이스케일 맵 생성:

`pgmramp -rectangle > {{경로/대상/출력.pgm}}`

- 타원형 그레이스케일 맵 생성:

`pgmramp -ellipse {{경로/대상/이미지.pgm}} > {{경로/대상/출력.pgm}}`

- 왼쪽 상단에서 오른쪽 하단으로 그레이스케일 맵 생성:

`pgmramp -diagonal {{경로/대상/이미지.pgm}} > {{경로/대상/출력.pgm}}`
