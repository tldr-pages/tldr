# unflatten

> 방향 그래프의 레이아웃 가로 세로 비율을 개선하기 위해 조정.
> Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> 더 많은 정보: <https://www.graphviz.org/pdf/unflatten.1.pdf>.

- 하나 이상의 방향 그래프를 조정하여 레이아웃 가로 세로 비율을 개선:

`unflatten {{경로/대상/input1.gv}} {{경로/대상/input2.gv ...}} > {{경로/대상/output.gv}}`

- `unflatten`을 `dot` 레이아웃 전처리기로 사용하여 가로 세로 비율 개선:

`unflatten {{경로/대상/입력.gv}} | dot -T {{png}} {{경로/대상/출력.png}}`

- 도움말 표시:

`unflatten -?`
