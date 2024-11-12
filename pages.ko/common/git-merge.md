# git merge

> 브랜치를 병합합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-merge>.

- 현재 브랜치에 브랜치 병합:

`git merge {{브랜치_이름}}`

- 병합 메시지 편집:

`git merge --edit {{브랜치_이름}}`

- 브랜치 병합 및 병합 커밋 생성:

`git merge --no-ff {{브랜치_이름}}`

- 충돌이 발생한 경우 병합 중단:

`git merge --abort`

- 특정 전략을 사용하여 병합:

`git merge --strategy {{전략}} --strategy-option {{전략_옵션}} {{브랜치_이름}}`
