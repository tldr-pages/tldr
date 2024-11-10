# nop

> 그래프의 유효성을 검사하고 정규 형식으로 예쁘게 출력.
> Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> 더 많은 정보: <https://www.graphviz.org/pdf/nop.1.pdf>.

- 하나 이상의 그래프를 정규 형식으로 예쁘게 출력:

`nop {{경로/대상/입력1.gv}} {{경로/대상/입력2.gv ...}} > {{경로/대상/출력.gv}}`

- 하나 이상의 그래프 유효성 검사, 출력 그래프는 생성하지 않음:

`nop -p {{경로/대상/입력1.gv}} {{경로/대상/입력2.gv ...}}`

- 도움말 표시:

`nop -?`
