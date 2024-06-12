# git branch

> 브랜치 작업을 위한 주요 Git 명령어.
> 더 많은 정보: <https://git-scm.com/docs/git-branch>.

- 모든 브랜치(로컬 및 원격; 현재 브랜치는 `*`로 강조됨) 나열:

`git branch --all`

- 특정 Git 커밋을 기록에 포함하는 브랜치 나열:

`git branch --all --contains {{커밋_해시}}`

- 현재 브랜치의 이름 표시:

`git branch --show-current`

- 현재 커밋을 기반으로 새로운 브랜치 생성:

`git branch {{브랜치_이름}}`

- 특정 커밋을 기반으로 새로운 브랜치 생성:

`git branch {{브랜치_이름}} {{커밋_해시}}`

- 브랜치 이름 변경 (체크아웃되지 않은 상태여야 함):

`git branch -m {{이전_브랜치_이름}} {{새로운_브랜치_이름}}`

- 로컬 브랜치 삭제 (체크아웃되지 않은 상태여야 함):

`git branch -d {{브랜치_이름}}`

- 원격 브랜치 삭제:

`git push {{원격_이름}} --delete {{원격_브랜치_이름}}`
