# git sync

> 로컬 브랜치를 원격 브랜치와 동기화.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-sync>.

- 현재 로컬 브랜치를 해당 원격 브랜치와 동기화:

`git sync`

- 현재 로컬 브랜치를 원격 main 브랜치와 동기화:

`git sync origin main`

- 추적되지 않은 파일을 삭제하지 않고 동기화:

`git sync {{[-s|--soft]}} {{원격_이름}} {{브랜치_이름}}`
