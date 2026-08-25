# latexmk

> LaTeX 소스 파일을 최종 문서로 컴파일.
> 필요한 경우 여러 번 자동 실행하여 문서 생성.
> 더 많은 정보: <https://mg.readthedocs.io/latexmk.html>.

- 모든 소스로부터 DVI (Device Independent 파일) 문서 컴파일:

`latexmk`

- 특정 소스 파일로부터 DVI 문서 컴파일:

`latexmk {{경로/대상/소스파일.tex}}`

- PDF 문서 컴파일:

`latexmk -pdf {{경로/대상/소스파일.tex}}`

- 문서를 뷰어로 열고, 소스 파일 변경 시 자동으로 재컴파일 및 갱신:

`latexmk -pvc {{경로/대상/소스파일.tex}}`

- 오류가 있어도 문서 생성을 강제 수행:

`latexmk -f {{경로/대상/소스파일.tex}}`

- 특정 TEX 파일에 대해 생성된 임시 파일 정리:

`latexmk -c {{경로/대상/소스파일.tex}}`

- 현재 디렉터리의 모든 임시 파일 정리:

`latexmk -c`

- 소스 파일과 사용자 리소스를 제외한 LaTeX 생성 파일 전체 정리:

`latexmk -C`
