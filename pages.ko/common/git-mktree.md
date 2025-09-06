# git mktree

> `ls-tree` 형식의 텍스트를 사용하여 트리 객체를 생성합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-mktree>.

- 트리 객체를 생성하고 각 트리 항목의 해시가 기존 객체를 식별하는지 확인:

`git mktree`

- 누락된 객체 허용:

`git mktree --missing`

- 트리 객체의 NUL([z]ero character)로 종료된 출력을 읽기 (`ls-tree -z`):

`git mktree -z`

- 여러 트리 객체 생성 허용:

`git mktree --batch`

- `stdin`에서 정렬하여 트리 생성 (비재귀 `git ls-tree` 출력 형식 필요):

`git mktree < {{경로/대상/tree.txt}}`
