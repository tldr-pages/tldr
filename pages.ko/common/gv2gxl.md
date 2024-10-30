# gv2gxl

> 그래프를 `gv`에서 `gxl` 형식으로 변환.
> 변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> 더 많은 정보: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- 그래프를 `gv`에서 `gxl` 형식으로 변환:

`gv2gxl -o {{출력.gxl}} {{입력.gv}}`

- `stdin` 및 `stdout`을 사용하여 그래프를 반환:

`cat {{입력.gv}} | gv2gxl > {{출력.gxl}}`

- 도움말 표시:

`gv2gxl -?`
