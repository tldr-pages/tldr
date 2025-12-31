# texliveonfly

> `.tex` 파일을 컴파일하는 동안 누락된 TeX Live 패키지를 다운로드.
> 더 많은 정보: <https://ctan.org/tex-archive/support/texliveonfly>.

- 컴파일하는 동안 누락된 패키지 다운로드:

`texliveonfly {{소스.tex}}`

- 특정 컴파일러 사용 (`pdflatex`가 기본값):

`texliveonfly --compiler={{컴파일러}} {{소스.tex}}`

- 사용자 지정 TeX Live `bin` 폴더 사용:

`texliveonfly --texlive_bin={{경로/대상/texlive_bin}} {{소스.tex}}`
