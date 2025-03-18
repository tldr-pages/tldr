# git revert

> 이전 커밋의 영향을 되돌리는 새로운 커밋을 생성합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-revert>.

- 가장 최근 커밋 되돌리기:

`git revert {{HEAD}}`

- 마지막에서 5번째 커밋 되돌리기:

`git revert HEAD~{{4}}`

- 특정 커밋 되돌리기:

`git revert {{0c01a9}}`

- 여러 커밋 되돌리기:

`git revert {{branch_name~5..branch_name~2}}`

- 새로운 커밋을 생성하지 않고 작업 트리만 변경:

`git revert {{[-n|--no-commit]}} {{0c01a9..9a1743}}`
