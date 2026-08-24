# elasticsearch-users

> Elasticsearch의 네이티브 영역 사용자(계정)를 생성, 수정, 삭제하는 도구.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/users-command>.

- 새로운 사용자 추가 (비밀번호 입력 프롬프트 표시):

`elasticsearch-users useradd {{사용자명}}`

- 역할을 지정하여 새로운 사용자 추가:

`elasticsearch-users useradd {{사용자명}} -r {{역할1,역할2}}`

- 기존 사용자 비밀번호 변경:

`elasticsearch-users passwd {{사용자명}}`

- 사용자 삭제:

`elasticsearch-users userdel {{사용자명}}`

- 네이티브 영역의 모든 사용자 목록 출력:

`elasticsearch-users list`
