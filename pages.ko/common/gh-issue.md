# gh issue

> GitHub 이슈 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_issue>.

- 특정 이슈 보기:

`gh issue view {{이슈_번호}}`

- 기본 웹 브라우저에서 특정 이슈 보기:

`gh issue view {{이슈_번호}} --web`

- 기본 웹 브라우저에서 새 이슈 생성:

`gh issue create --web`

- `bug` 라벨이 있는 최근 10개의 이슈 나열:

`gh issue list --limit {{10}} --label "{{bug}}"`

- 특정 사용자가 만든 닫힌 이슈 나열:

`gh issue list --state closed --author {{사용자_명}}`

- 특정 저장소의 사용자와 관련된 이슈 상태 표시:

`gh issue status --repo {{소유자}}/{{저장소}}`

- 특정 이슈 다시 열기:

`gh issue reopen {{이슈_번호}}`
