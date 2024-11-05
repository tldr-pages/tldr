# graphml2gv

> 그래프를 `graphml`에서 `gv` 형식으로 변환.
> 변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> 더 많은 정보: <https://graphviz.org/pdf/graphml2gv.1.pdf>.

- 그래프를 `gml`에서 `gv` 형식으로 변환:

`graphml2gv -o {{출력.gv}} {{input.gml}}`

- `stdin` 및 `stdout`을 사용하여 그래프를 변환:

`cat {{input.gml}} | graphml2gv > {{출력.gv}}`

- 도움말 표시:

`graphml2gv -?`
