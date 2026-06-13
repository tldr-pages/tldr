# latex

> LaTeX 소스 파일에서 DVI 문서를 컴파일합니다.
> 더 많은 정보: <https://texdoc.org/serve/tex.man1.pdf/0>.

- DVI 문서 컴파일:

`latex {{소스.tex}}`

- 출력 디렉토리를 지정하여 DVI 문서 컴파일:

`latex -output-directory={{경로/대상/폴더}} {{소스.tex}}`

- 각 오류 발생 시 종료하며 DVI 문서 컴파일:

`latex -halt-on-error {{소스.tex}}`
