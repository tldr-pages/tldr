# acyclic

> 일부 간선을 반전시켜 방향성 그래프를 순환이 없는 그래프로 변환합니다.
> Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> 더 많은 정보: <https://graphviz.org/pdf/acyclic.1.pdf>.

- 일부 간선을 반전시켜 방향성 그래프를 순환이 없는 그래프로 변환:

`acyclic {{경로/대상/입력.gv}} > {{경로/대상/출력.gv}}`

- 그래프가 순환이 없거나 주기가 있거나 방향이 지정되지 않아 출력 그래프가 생성되지 않는 경우 출력:

`acyclic -v -n {{경로/대상/입력.gv}}`

- `acyclic`의 도움말 표시:

`acyclic -?`
