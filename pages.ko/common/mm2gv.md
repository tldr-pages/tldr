# mm2gv

> 그래프를 Matrix Market `mm` 형식에서 `gv` 형식으로 변환.
> 변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> 더 많은 정보: <https://graphviz.org/pdf/mm2gv.1.pdf>.

- 그래프를 `mm` 형식에서 `gv` 형식으로 변환:

`mm2gv -o {{출력.gv}} {{입력.mm}}`

- `stdin`과 `stdout`을 사용하여 그래프 변환:

`cat {{입력.mm}} | mm2gv > {{출력.gv}}`

- 도움말 표시:

`mm2gv -?`
