# gh search

> GitHub 전체에서 검색 수행.
> 더 많은 정보: <https://cli.github.com/manual/gh_search>.

- 특정 키워드를 포함한 코드 검색:

`gh search code {{키워드1 키워드2 ...}}`

- 특정 문구를 포함한 이슈 검색:

`gh search issues "{{검색_문자열}}"`

- 특정 작성자의 커밋 검색:

`gh search commits --author {{사용자명}}`

- 자신에게 할당되어 있으며 아직 열려 있는 Pull Request 검색:

`gh search prs --assignee @me --state open`

- 조직 내 특정 토픽(topic)을 가진 저장소 검색:

`gh search repos --owner {{조직_이름}} --topic {{주제_이름}}`

- 특정 라벨이 없는 이슈 검색 (Unix 계열 시스템):

`gh search issues -- "{{검색_쿼리}} -label:{{라벨_이름}}"`

- 특정 라벨이 없는 이슈 검색 (PowerShell):

`gh --% search issues -- "{{검색_쿼리}} -label:{{라벨_이름}}"`

- 검색 쿼리를 웹 브라우저에서 열기:

`gh search {{하위명령어}} {{[-w|--web]}} {{쿼리}}`
