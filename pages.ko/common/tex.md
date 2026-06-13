# tex

> TeX 소스 파일에서 DVI 문서를 컴파일.
> 더 많은 정보: <https://www.tug.org/begin.html>.

- DVI 문서 컴파일:

`tex {{소스.tex}}`

- 출력 폴더를 지정하여 DVI 문서 컴파일:

`tex -output-directory={{경로/대상/폴더}} {{소스.tex}}`

- 각 오류 발생 시 종료하며 DVI 문서 컴파일:

`tex -halt-on-error {{소스.tex}}`
