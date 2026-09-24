# gvgen

> 단순하고 구조화된 추상 그래프 생성.
> 더 많은 정보: <https://graphviz.org/pdf/gvgen.1.pdf>.

- 정점과 엣지가 10개인 사이클([c]ycle) 그래프 생성 후 `stdout`에 출력:

`gvgen -c {{10}}`

- 4×3 그리드([g]rid):

`gvgen -g {{4,3}}`

- 높이 5의 이진트리([t]ree) 생성:

`gvgen -t {{5}}`

- 정점이 각각 3개와 4개인 완전 이분 그래프([b]ipartite graph):

`gvgen -b {{3,4}}`

- 랜덤([r]andom) 그래프 생성 후 파일로 출력([o]utput):

`gvgen -r {{10,5}} -o {{random.gv}}`

- 방향([d]irected) 그래프를 자세한([v]erbose) 출력과 함께 생성:

`gvgen -d -v -c {{6}}`

- 도움말 표시:

`gvgen -?`
