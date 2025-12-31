# gh

> GitHub와 원활하게 작업.
> `config`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://cli.github.com/manual/gh>.

- GitHub 리포지토리를 로컬에 복제:

`gh repo clone {{소유자}}/{{리포지토리}}`

- 새 이슈 생성:

`gh issue {{[new|create]}}`

- 현재 리포지토리의 열린 이슈를 보고 필터링:

`gh issue {{[ls|list]}}`

- 기본 웹 브라우저에서 이슈 보기:

`gh issue view {{[-w|--web]}} {{이슈_번호}}`

- 풀 리퀘스트 생성:

`gh pr {{[new|create]}}`

- 기본 웹 브라우저에서 풀 리퀘스트 보기:

`gh pr view {{[-w|--web]}} {{pr_번호}}`

- 특정 풀 리퀘스트를 로컬에 체크아웃:

`gh {{[co|pr checkout]}} {{pr_번호}}`

- 리포지토리의 풀 리퀘스트 상태 확인:

`gh pr status`
