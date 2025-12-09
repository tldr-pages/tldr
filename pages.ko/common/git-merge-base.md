# git merge-base

> 두 커밋의 공통 조상을 찾습니다.
> 더 많은 정보: <https://git-scm.com/docs/git-merge-base>.

- 두 커밋의 최상의 공통 조상을 출력:

`git merge-base {{commit_1}} {{commit_2}}`

- 두 커밋의 모든 최상의 공통 조상을 출력:

`git merge-base --all {{commit_1}} {{commit_2}}`

- 특정 커밋이 다른 커밋의 조상인지 확인:

`git merge-base --is-ancestor {{ancestor_commit}} {{commit}}`
