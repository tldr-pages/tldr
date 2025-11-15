# mingle

> 그래프 레이아웃의 엣지를 번들링.
> Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> 더 많은 정보: <https://www.graphviz.org/pdf/mingle.1.pdf>.

- 하나 이상의 그래프 레이아웃(이미 레이아웃 정보가 있는)의 엣지를 번들링:

`mingle {{경로/대상/레이아웃1.gv}} {{경로/대상/레이아웃2.gv ...}} > {{경로/대상/출력.gv}}`

- 레이아웃, 번들링을 수행하고 한 번의 명령으로 그림으로 출력:

`dot {{경로/대상/입력.gv}} | mingle | dot -T {{png}} > {{경로/대상/출력.png}}`

- 도움말 표시:

`mingle -?`
