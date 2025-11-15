# latexmk

> LaTeX 소스 파일을 완성된 문서로 컴파일.
> 필요에 따라 자동으로 여러 번 실행.
> 더 많은 정보: <https://mg.readthedocs.io/latexmk.html>.

- 모든 소스에서 DVI(장치 독립 파일) 문서 컴파일:

`latexmk`

- 특정 소스 파일에서 DVI 문서 컴파일:

`latexmk {{경로/대상/소스.tex}}`

- PDF 문서 컴파일:

`latexmk -pdf {{경로/대상/소스.tex}}`

- 문서를 뷰어에서 열고 소스 파일이 변경될 때마다 지속적으로 업데이트:

`latexmk -pvc {{경로/대상/소스.tex}}`

- 오류가 있어도 문서 생성을 강제:

`latexmk -f {{경로/대상/소스.tex}}`

- 특정 TEX 파일에 대해 생성된 임시 TEX 파일 정리:

`latexmk -c {{경로/대상/소스.tex}}`

- 현재 디렉토리의 모든 임시 TEX 파일 정리:

`latexmk -c`
