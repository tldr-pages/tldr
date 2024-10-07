# git show-branch

> 브랜치와 해당 커밋을 표시.
> 더 많은 정보: <https://git-scm.com/docs/git-show-branch>.

- 브랜치의 최신 커밋 요약 표시:

`git show-branch {{브랜치_이름|참조|커밋}}`

- 여러 커밋 또는 브랜치의 히스토리 비교:

`git show-branch {{브랜치_이름1|참조1|커밋1 브랜치_이름2|참조2|커밋2 ...}}`

- 모든 원격 추적 브랜치 비교:

`git show-branch --remotes`

- 로컬 및 원격 추적 브랜치 모두 비교:

`git show-branch --all`

- 모든 브랜치의 최신 커밋 나열:

`git show-branch --all --list`

- 현재 브랜치와 특정 브랜치 비교:

`git show-branch --current {{커밋|브랜치_이름|참조}}`

- 상대적 이름 대신 커밋 이름 표시:

`git show-branch --sha1-name --current {{현재|브랜치_이름|참조}}`

- 공통 조상 이후의 커밋을 주어진 숫자만큼 계속 표시:

`git show-branch --more {{5}} {{커밋|브랜치_이름|참조}} {{커밋|브랜치_이름|참조}} {{...}}`
