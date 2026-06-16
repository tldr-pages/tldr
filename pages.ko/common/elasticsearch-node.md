# elasticsearch-node

> 노드 종료, 재구성, 정보 조회 등 Elasticsearch 노드의 저수준 작업을 관리하는 도구.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/node-tool>.

- 현재 노드 정보 출력:

`elasticsearch-node info`

- 전체 클러스터 재시작을 위한 노드 준비 (예: 업그레이드 후):

`elasticsearch-node unsafe-bootstrap`

- 노드 역할 변경을 위한 재구성 (예: master에서 data 노드):

`elasticsearch-node repurpose`

- 노드에 할당된 역할 목록 출력:

`elasticsearch-node roles`

- JVM 버전, Elasticsearch 홈 경로 등 진단 정보 출력:

`elasticsearch-node diagnostics`

- 도움말 표시:

`elasticsearch-node {{[-h|--help]}}`
