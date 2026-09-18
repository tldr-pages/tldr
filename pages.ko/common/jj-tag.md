# jj tag

> `jj` 저장소의 태그를 관리.
> `delete`, `list`, `set` 등의 일부 하위 명령은 각각 별도의 사용 문서를 제공.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag>.

- 현재 작업 복사본 리비전을 가리키는 태그 생성:

`jj tag {{[s|set]}} {{태그_이름}}`

- 지정한 리비전을 가리키는 태그 생성:

`jj tag {{[s|set]}} {{태그_이름}} {{[-r|--revision]}} {{revision}}`

- 모든 태그 목록 표시:

`jj tag {{[l|list]}}`

- 패턴과 일치하는 태그를 커미터 날짜 기준(최신순)으로 정렬하여 표시:

`jj tag {{[l|list]}} --sort committer-date- "{{패턴}}"`

- 기존 태그를 다른 리비전으로 이동:

`jj tag {{[s|set]}} {{tag_name}} {{[-r|--revision]}} {{revision}} --allow-move`

- 태그 삭제:

`jj tag {{[d|delete]}} {{태그_이름}}`

- glob 패턴과 일치하는 태그 삭제:

`jj tag {{[d|delete]}} "{{glob:v1.*}}"`

- 도움말 표시:

`jj tag {{[-h|--help]}}`
