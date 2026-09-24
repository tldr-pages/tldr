# gc

> Graphviz `.dot` 파일에서 노드, 엣지, 컴포넌트, 클러스터 개수를 계산.
> 더 많은 정보: <https://graphviz.org/pdf/gc.1.pdf>.

- 파일의 노드와 엣지 개수 계산:

`gc {{경로/대상/파일.dot}}`

- 노드([n]odes) 개수만 계산:

`gc -n {{경로/대상/파일.dot}}`

- 엣지([e]dges) 개수만 계산:

`gc -e {{경로/대상/파일.dot}}`

- 연결된([c]onnected) 컴포넌트 개수 계산:

`gc -c {{경로/대상/파일.dot}}`

- 도움말 표시:

`gc -?`
