# edgepaint

> 교차하는 가장자리를 명확하게 하기 위해, 그래프 레이아웃의 가장자리에 색상을 지정.
> Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> 더 많은 정보: <https://graphviz.org/pdf/edgepaint.1.pdf>.

- 하나 이상의 그래프 레이아웃 (이미 레이아웃 정보가 있음)의 가장자리에 색상을 지정하여, 교차하는 가장자리를 명확하게 함:

`edgepaint {{경로/대상/레이아웃1.gv}} {{경로/대상/레이아웃2.gv ...}} > {{경로/대상/출력파일.gv}}`

- 색 구성표를 사용하여 가장자리에 색상을 지정. (<https://graphviz.org/doc/info/colors.html#brewer> 참조):

`edgepaint -color-scheme={{accent7}} {{경로/대상/레이아웃.gv}} > {{경로/대상/출력파일.gv}}`

- 그래프를 배치하고 가장자리에 색상을 지정한다음, PNG 이미지로 변환:

`dot {{경로/대상/입력파일.gv}} | edgepaint | dot -T {{png}} > {{경로/대상/출력파일.png}}`

- 도움말 표시:

`edgepaint -?`
