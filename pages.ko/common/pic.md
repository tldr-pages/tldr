# pic

> groff (GNU Troff) 문서 형식 시스템을 위한 그림 전처리기.
> 같이 보기: `groff`, `troff`.
> 더 많은 정보: <https://manned.org/pic>.

- 그림이 포함된 입력을 처리하고, 나중에 groff를 사용하여 PostScript로 조판하기 위해 출력 저장:

`pic {{경로/대상/입력.pic}} > {{경로/대상/출력.roff}}`

- [me] 매크로 패키지를 사용하여 그림이 포함된 입력을 PDF로 조판:

`pic -T {{pdf}} {{경로/대상/입력.pic}} | groff -{{me}} -T {{pdf}} > {{경로/대상/출력.pdf}}`
