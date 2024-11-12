# gh issue create

> 저장소에 GitHub 이슈 생성.
> 더 많은 정보: <https://cli.github.com/manual/gh_issue_create>.

- 현재 저장소에 대해 대화식으로 새 이슈 생성:

`gh issue create`

- `bug` 레이블을 사용하여 대화식으로 새 이슈 생성:

`gh issue create --label "{{bug}}"`

- 지정된 사용자에게 할당하여 대화식으로 새 이슈 생성:

`gh issue create --assignee {{user1,user2,...}}`

- 제목과 본문을 지정하고 현재 사용자에게 할당하여 새 이슈 생성:

`gh issue create --title "{{제목}}" --body "{{본문}}" --assignee "{{@me}}"`

- 파일에서 본문 텍스트를 읽어와 대화식으로 새 이슈 생성:

`gh issue create --body-file {{경로/대상/파일}}`

- 기본 웹 브라우저에서 새 이슈 생성:

`gh issue create --web`

- 도움말 표시:

`gh issue create --help`
