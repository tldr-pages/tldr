# gml2gv

> 그래프를 `gml`에서 `gv` 형식으로 변환.
> 변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> 더 많은 정보: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- 그래프를 `gml`에서 `gv` 형식으로 변환:

`gml2gv -o {{output.gv}} {{입력파일.gml}}`

- `stdin` 및 `stdout`을 사용하여 그래프를 반환:

`cat {{입력파일.gml}} | gml2gv > {{output.gv}}`

- 도움말 표시:

`gml2gv -?`
