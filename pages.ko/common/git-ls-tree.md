# git ls-tree

> 트리 객체의 파일과 디렉토리 목록을 보여줍니다.
> 더 많은 정보: <https://git-scm.com/docs/git-ls-tree>.

- 특정 브랜치의 파일과 디렉토리 목록 보기:

`git ls-tree {{브랜치_이름}}`

- 특정 커밋의 파일과 디렉토리 목록을 하위 디렉토리까지 재귀적으로 보기:

`git ls-tree -r {{커밋_해시}}`

- 특정 커밋의 파일 이름만 보기:

`git ls-tree --name-only {{커밋_해시}}`

- 현재 브랜치의 최신 상태 파일과 디렉토리 목록을 트리 구조로 출력하기 (참고: `tree --fromfile`은 Windows에서 지원되지 않음):

`git ls-tree -r --name-only HEAD | tree --fromfile`
