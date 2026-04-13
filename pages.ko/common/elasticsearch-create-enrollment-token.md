# elasticsearch-create-enrollment-token

> Elasticsearch 노드 및 Kibana 인스턴스를 위한 등록 토큰을 생성하는 도구.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/create-enrollment-token>.

- 새로운 Elasticsearch 노드 추가를 위한 등록 토큰 생성:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node`

- 새로운 Kibana 인스턴스 추가를 위한 등록 토큰 생성:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana`

- 상세 출력과 함께 등록 토큰 생성:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node --verbose`

- 사용자 정의 Elasticsearch URL을 사용하여 Kibana용 등록 토큰 생성:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana --url "{{IP}}"`

- 도움말 표시:

`elasticsearch-create-enrollment-token {{[-h|--help]}}`
