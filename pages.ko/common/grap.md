# grap

> groff (GNU Troff) 문서 형식화 시스템을 위한 차트 작성 전처리기.
> `pic` 및 `groff`를 참고.
> 더 많은 정보: <https://manned.org/grap>.

- `grap` 파일을 처리하고 `pic` 및 `groff`를 사용하여 향후 처리를 위해 출력 파일을 저장:

`grap {{경로/대상/입력파일.grap}} > {{경로/대상/출력파일.pic}}`

- [me] 매크로 패키지를 사용하여 `grap` 파일을 PDF로 조판하고, 출력을 파일에 저장:

`grap {{경로/대상/입력파일.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{경로/대상/출력파일.pdf}}`
