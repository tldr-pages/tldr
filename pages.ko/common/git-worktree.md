# git worktree

> 동일한 저장소에 연결된 여러 작업 트리를 관리.
> 더 많은 정보: <https://git-scm.com/docs/git-worktree>.

- 지정된 브랜치가 체크아웃된 새 디렉터리 생성:

`git worktree add {{경로/대상/폴더}} {{브랜치}}`

- 새로운 브랜치가 체크아웃된 새 디렉터리 생성:

`git worktree add {{경로/대상/폴더}} -b {{새_브랜치}}`

- 이 저장소에 연결된 모든 작업 디렉터리 나열:

`git worktree list`

- 작업 트리 제거 (작업 트리 디렉터리 삭제 후):

`git worktree prune`
