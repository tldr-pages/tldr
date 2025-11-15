# pdflatex

> LaTeX 소스 파일을 PDF 문서로 컴파일.
> 더 많은 정보: <https://manned.org/pdflatex>.

- PDF 문서 컴파일:

`pdflatex {{소스.tex}}`

- 출력 디렉토리를 지정하여 PDF 문서 컴파일:

`pdflatex -output-directory={{경로/대상/폴더}} {{소스.tex}}`

- 각 오류에서 중지하며 PDF 문서 컴파일:

`pdflatex -halt-on-error {{소스.tex}}`
