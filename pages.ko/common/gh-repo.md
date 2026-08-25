# gh repo

> GitHub 저장소 작업 수행.
> 더 많은 정보: <https://cli.github.com/manual/gh_repo>.

- 새로운 저장소를 대화형으로 생성:

`gh repo {{[new|create]}}`

- 저장소 복제:

`gh repo clone {{소유자}}/{{저장소}}`

- 저장소를 fork 후 clone 수행:

`gh repo fork {{소유자}}/{{저장소}} --clone`

- 기본 웹 브라우저에서 저장소 보기:

`gh repo view {{저장소}} {{[-w|--web]}}`

- 특정 사용자 또는 조직이 소유한 저장소 목록 표시 (소유자를 지정하지 않으면, 현재 로그인한 사용자 사용):

`gh repo {{[ls|list]}} {{소유자}}`

- fork가 아닌 저장소만 표시하고 목록 개수 제한 (기본값: 30):

`gh repo {{[ls|list]}} {{소유자}} --source {{[-L|--limit]}} {{제한_개수}}`

- 특정 주 사용 언어를 가진 저장소 목록 표시:

`gh repo {{[ls|list]}} {{소유자}} {{[-l|--language]}} {{언어_이름}}`

- 현재 로컬 저장소를 upstream과 동기화:

`gh repo sync`
