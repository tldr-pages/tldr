# glab

> GitLab으로 원활하게 작업.
> `config`와 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
> 더 많은 정보: <https://gitlab.com/gitlab-org/cli/-/tree/main/docs/source>.

- 로컬에서 GitLab 저장소를 복제:

`glab repo clone {{소유자}}/{{레포지토리}}`

- 새로운 이슈 생성:

`glab issue create`

- 현재 저장소의 공개 이슈를 보고 필터링:

`glab issue list`

- 기본 브라우저에서 이슈 보기:

`glab issue view {{[-w|--web]}} {{이슈_번호}}`

- 병합 요청을 생성:

`glab mr create`

- 기본 웹 브라우저에서 풀 요청 보기:

`glab mr view {{[-w|--web]}} {{pr_번호}}`

- 특정 풀 요청을 로컬에서 확인:

`glab mr checkout {{pr_번호}}`
