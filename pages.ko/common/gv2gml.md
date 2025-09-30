# gv2gml

> 그래프를 `gv`에서 `gml`형식으로 변환.
> 변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> 더 많은 정보: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- 그래프를 `gv`에서 `gml`형식으로 변환.:

`gv2gml -o {{output.gml}} {{input.gv}}`

- `stdin` 및 `stdout` 사용하여 그래프를 변환:

`cat {{입력.gv}} | gv2gml > {{출력.gml}}`

- 도움말 표시:

`gv2gml -?`
