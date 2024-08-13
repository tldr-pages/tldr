# git switch

> Git 브랜치 간 전환합니다. Git 버전 2.23+가 필요합니다.
> 같이 보기: `git checkout`.
> 더 많은 정보: <https://git-scm.com/docs/git-switch>.

- 기존 브랜치로 전환:

`git switch {{브랜치_이름}}`

- 새 브랜치를 만들고 전환:

`git switch --create {{브랜치_이름}}`

- 기존 커밋을 기반으로 새 브랜치를 만들고 전환:

`git switch --create {{브랜치_이름}} {{커밋}}`

- 이전 브랜치로 전환:

`git switch -`

- 브랜치로 전환하고 모든 서브모듈을 일치하도록 업데이트:

`git switch --recurse-submodules {{브랜치_이름}}`

- 브랜치로 전환하고 현재 브랜치와 미커밋된 변경 사항을 자동으로 병합:

`git switch --merge {{브랜치_이름}}`
