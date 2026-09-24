# elasticsearch-keystore

> Elasticsearch에서 사용하는 보안 설정(예: 비밀번호, 토큰, 자격 증명 등)을 관리하는 도구.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-keystore>.

- 새로운 keystore 생성 (비밀번호 없음):

`elasticsearch-keystore create`

- 비밀번호로 보호된 keystore 생성:

`elasticsearch-keystore create -p`

- 설정을 대화형으로 추가:

`elasticsearch-keystore add {{설정_이름}}`

- `stdin`을 통해 설정 추가:

`echo "{{setting_value}}" | elasticsearch-keystore add --stdin {{설정_이름}}`

- keystore에서 설정 제거:

`elasticsearch-keystore remove {{설정_이름}}`

- keystore 비밀번호 변경:

`elasticsearch-keystore passwd`

- keystore에 저장된 모든 설정 목록 출력:

`elasticsearch-keystore list`

- keystore 포맷 업그레이드 (Elasticsearch 업그레이드 후):

`elasticsearch-keystore upgrade`
