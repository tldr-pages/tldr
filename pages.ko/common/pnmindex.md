# pnmindex

> 여러 PNM 이미지의 시각적 색인을 생성합니다.
> 같이 보기: `pamundice`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmindex.html>.

- 지정된 이미지를 그리드 형식으로 축소판 이미지로 포함하는 이미지를 생성:

`pnmindex {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pnm}}`

- 축소판 이미지의 (정사각형) 크기 지정:

`pnmindex -size {{50}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pnm}}`

- 한 행에 표시할 축소판 이미지의 개수 지정:

`pnmindex -across {{10}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pnm}}`

- 출력 이미지의 최대 색상 수 지정:

`pnmindex -colors {{512}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pnm}}`
