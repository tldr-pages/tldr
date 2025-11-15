# sccmap

> 방향 그래프의 강하게 연결된 컴포넌트를 추출합니다.
> Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> 더 많은 정보: <https://www.graphviz.org/pdf/sccmap.1.pdf>.

- 하나 이상의 방향 그래프에서 강하게 연결된 컴포넌트 추출:

`sccmap -S {{경로/대상/입력1.gv}} {{경로/대상/입력2.gv ...}} > {{경로/대상/출력.gv}}`

- 그래프에 대한 통계를 출력하며, 그래프 출력은 생성하지 않음:

`sccmap -v -s {{경로/대상/입력1.gv}} {{경로/대상/입력2.gv ...}}`

- 도움말 표시:

`sccmap -?`
