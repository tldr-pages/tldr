# gh pr

> GitHub 풀 리퀘스트를 관리.
> `create`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://cli.github.com/manual/gh_pr>.

- 풀 리퀘스트 생성:

`gh pr create`

- 특정 풀 리퀘스트를 로컬에서 체크아웃:

`gh pr checkout {{pr_number}}`

- 현재 브랜치의 풀 리퀘스트에서 변경 사항 보기:

`gh pr diff`

- 현재 브랜치의 풀 리퀘스트 승인:

`gh pr review --approve`

- 현재 브랜치와 연관된 풀 리퀘스트를 대화식으로 병합:

`gh pr merge`

- 풀 리퀘스트를 대화식으로 수정:

`gh pr edit`

- 풀 리퀘스트의 기준 브랜치 수정:

`gh pr edit --base {{branch_name}}`

- 현재 저장소의 풀 리퀘스트 상태 확인:

`gh pr status`
