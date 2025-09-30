# hub issue

> Github 이슈를 관리.
> 더 많은 정보: <https://hub.github.com/hub-issue.1.html>.

- `bug` 라벨이 있는 최근 10개 문제를 나열:

`hub issue list --limit {{10}} --labels "{{bug}}"`

- 특정 문제를 표시:

`hub issue show {{이슈_번호}}`

- 특정 사용자에게 할당된 10개의 종결된 문제를 나열:

`hub issue --state {{closed}} --assignee {{사용자명}} --limit {{10}}`
