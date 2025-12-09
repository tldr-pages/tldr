# lualatex

> Lua를 사용하여 컴파일하는 TeX의 확장 버전.
> 더 많은 정보: <https://texdoc.org/serve/tex.man1.pdf/0>.

- Lua 인터프리터로 작동하도록 `texlua` 시작:

`lualatex`

- Tex 파일을 PDF로 컴파일:

`lualatex {{경로/대상/파일.tex}}`

- 오류로 중단 없이 Tex 파일 컴파일:

`lualatex -interaction nonstopmode {{경로/대상/파일.tex}}`

- 특정 출력 파일 이름으로 Tex 파일 컴파일:

`lualatex -jobname={{파일이름}} {{경로/대상/파일.tex}}`
