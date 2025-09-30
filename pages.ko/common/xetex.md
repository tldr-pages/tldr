# xetex

> XeTeX 소스 파일에서 PDF 문서를 컴파일.
> 더 많은 정보: <https://www.tug.org/xetex/>.

- PDF 문서 컴파일:

`xetex {{소스.tex}}`

- 출력 디렉토리를 지정하여 PDF 문서 컴파일:

`xetex -output-directory={{경로/대상/폴더}} {{소스.tex}}`

- 오류 발생 시 종료하며 PDF 문서 컴파일:

`xetex -halt-on-error {{소스.tex}}`
