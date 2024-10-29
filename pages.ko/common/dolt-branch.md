# dolt branch

> Dolt 브랜치를 관리.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-branch>.

- 로컬 브랜치 목록 표시 (현재 브랜치는 `*`로 강조 표시됨):

`dolt branch`

- 모든 로컬 및 원격 브랜치 목록 표시:

`dolt branch --all`

- 현재 브랜치를 기반으로 새 브랜치 생성:

`dolt branch {{브랜치_이름}}`

- 지정된 커밋을 최신으로 하여 새 브랜치 생성:

`dolt branch {{브랜치_이름}} {{커밋}}`

- 브랜치 이름 변경:

`dolt branch --move {{브랜치_이름1}} {{브랜치_이름2}}`

- 브랜치 복제:

`dolt branch --copy {{브랜치_이름1}} {{브랜치_이름2}}`

- 브랜치 삭제:

`dolt branch --delete {{브랜치_이름}}`

- 현재 브랜치 이름 표시:

`dolt branch --show-current`
