# gh repo

> GitHub 저장소 작업.
> 더 많은 정보: <https://cli.github.com/manual/gh_repo>.

- 새 저장소 생성 (저장소 이름이 설정되지 않으면, 기본 이름은 현재 디렉토리 이름이 됨):

`gh repo create {{이름}}`

- 저장소 복제:

`gh repo clone {{소유자}}/{{저장소}}`

- 저장소 포크 및 복제:

`gh repo fork {{소유자}}/{{저장소}} --clone`

- 기본 웹 브라우저에서 저장소 보기:

`gh repo view {{저장소}} --web`

- 특정 사용자 또는 조직이 소유한 저장소 나열 (소유자가 설정되지 않으면, 기본 소유자는 현재 로그인된 사용자):

`gh repo list {{소유자}}`

- 포크가 아닌 저장소만 나열하고 나열할 저장소 수 제한 (기본값: 30):

`gh repo list {{소유자}} --source -L {{제한}}`

- 특정 주요 코딩 언어가 있는 저장소 나열:

`gh repo list {{소유자}} --language {{언어_이름}}`
