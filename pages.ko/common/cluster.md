# cluster

> 그래프에서 클러스터를 찾고, 해당 정보를 그래프에 추가.
> 더 많은 정보: <https://graphviz.org/pdf/cluster.1.pdf>.

- 모듈러리티(modularity)를 최적화하는 클러스터를 생성하고 결과를 `stdout`으로 출력:

`cluster {{입력파일.gv}}`

- 생성할 클러스터([C]lusters) 수를 지정 (대략적인 값) (0이 기본값, 모듈러리티(modularity)를 대략적으로 최적화하는 개수가 선택됨):

`cluster -C {{5}} {{입력파일.gv}}`

- 다른 클러스터링([c]lustering) 방법을 사용 (0: 모듈러리티 클러스터링, 1: 모듈러리티 품질):

`cluster -c {{0|1}} {{입력파일.gv}}`

- 출력([o]utput)을 파일로 저장:

`cluster -o {{출력파일.gv}} {{입력파일.gv}}`

- 상세 출력([v]erbose) 모드를 활성화:

`cluster -v {{입력파일.gv}}`
