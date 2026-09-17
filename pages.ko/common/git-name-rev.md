# git name-rev

> 기존 ref 이름을 사용하여 커밋 설정.
> 더 많은 정보: <https://git-scm.com/docs/git-name-rev>.

- `HEAD`의 이름 표시:

`git name-rev HEAD`

- 이름만 표시:

`git name-rev --name-only HEAD`

- 일치하는 모든 ref 이름을 열거:

`git name-rev --all`

- 태그만 사용하여 커밋 이름 지정:

`git name-rev --tags HEAD`

- 알 수 없는 커밋에 대해 `undefined`를 출력하지 않고 non-zero 상태 코드로 종료:

`git name-rev --no-undefined {{commit-ish}}`

- 여러 커밋의 이름 표시:

`git name-rev HEAD~1 HEAD~2 main`

- 브랜치 ref만 사용하도록 제한:

`git name-rev --refs refs/heads/ {{commit-ish}}`

- `stdin`으로부터 커밋 ID 읽기:

`echo "{{commit-ish}}" | git name-rev --annotate-stdin`
