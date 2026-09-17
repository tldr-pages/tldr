# latexpand

> LaTeX 소스 파일을 단순화해 주석 제거 및 `\include`, `\input` 등을 실제 내용으로 펼침.
> 더 많은 정보: <https://www.ctan.org/pkg/latexpand>.

- 지정한 소스 파일을 단순화하고 결과를 출력 파일로 저장:

`latexpand {{[-o|--output]}} {{경로/대상/출력파일.tex}} {{경로/대상/파일.tex}}`

- 주석을 제거하지 않음:

`latexpand --keep-comments {{[-o|--output]}} {{경로/대상/출력파일.tex}} {{경로/대상/파일.tex}}`

- `\include`, `\input` 등을 확장하지 않음:

`latexpand --keep-includes {{[-o|--output]}} {{경로/대상/출력파일.tex}} {{경로/대상/파일.tex}}`

- 해당 STY 파일을 찾을 수 있는 경우, `\usepackage`까지 확장:

`latexpand --expand-usepackage {{[-o|--output]}} {{경로/대상/출력파일.tex}} {{경로/대상/파일.tex}}`

- 지정한 BBL 파일을 본문에 직접 포함:

`latexpand --expand-bbl {{경로/대상/bibliography.bbl}} {{[-o|--output]}} {{경로/대상/출력파일.tex}} {{경로/대상/파일.tex}}`
