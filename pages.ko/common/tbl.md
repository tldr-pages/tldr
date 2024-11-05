# tbl

> groff (GNU Troff) 문서 형식 시스템을 위한 테이블 전처리기.
> 같이 보기: `groff`, `troff`.
> 더 많은 정보: <https://manned.org/tbl>.

- 입력에 포함된 테이블을 처리하여, 후에 groff로 PostScript 형식으로 조판할 수 있도록 출력 저장:

`tbl {{경로/대상/입력_파일}} > {{경로/대상/출력.roff}}`

- [me] 매크로 패키지를 사용하여 테이블이 있는 입력을 PDF로 조판:

`tbl -T {{pdf}} {{경로/대상/입력.tbl}} | groff -{{me}} -T {{pdf}} > {{경로/대상/출력.pdf}}`
