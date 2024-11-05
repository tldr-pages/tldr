# pgmkernel

> `pnmconvol`과 함께 사용할 합성 커널을 생성.
> 같이 보기: `pnmconvol`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmkernel.html>.

- 합성 커널 생성:

`pgmkernel {{너비}} {{높이}} > {{경로/대상/출력.pgm}}`

- 정사각형 합성 커널 생성:

`pgmkernel {{크기}} > {{경로/대상/출력.pgm}}`

- 생성된 커널의 중앙 무게 지정:

`pgmkernel -weight {{값}} {{너비}} {{높이}} > {{경로/대상/출력.pgm}}`
