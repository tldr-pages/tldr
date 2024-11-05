# pgmhist

> PGM 이미지에 포함된 값의 히스토그램을 출력.
> 같이 보기: `ppmhist`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmhist.html>.

- 사람이 읽을 수 있는 히스토그램 표시:

`pgmhist {{경로/대상/이미지.pgm}}`

- 중간 회색 값 표시:

`pgmhist -median {{경로/대상/이미지.pgm}}`

- 네 개의 사분위수 회색 값 표시:

`pgmhist -quartile {{경로/대상/이미지.pgm}}`

- 잘못된 회색 값의 존재 여부 보고:

`pgmhist -forensic {{경로/대상/이미지.pgm}}`

- 기계가 읽을 수 있는 출력 표시:

`pgmhist -machine {{경로/대상/이미지.pgm}}`
