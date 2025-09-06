# gxl2gv

> 그래프를 `gxl`에서 `gv` 형식으로 변환.
> 변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> 더 많은 정보: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- 그래프를 `gxl`에서 `gv` 형식으로 변환:

`gxl2gv -o {{출력.gv}} {{입력.gxl}}`

- `stdin` 및 `stdout`을 사용하여 그래프를 변환:

`cat {{입력.gxl}} | gxl2gv > {{출력.gv}}`

- 도움말 표시:

`gxl2gv -?`
