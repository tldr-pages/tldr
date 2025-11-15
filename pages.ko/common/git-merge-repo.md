# git merge-repo

> 두 저장소의 히스토리를 병합.
> `git-extras`의 일부.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo>.

- 저장소의 브랜치를 현재 저장소의 디렉토리에 병합:

`git merge-repo {{경로/대상/저장소}} {{브랜치_이름}} {{경로/대상/폴더}}`

- 원격 저장소의 브랜치를 현재 저장소의 디렉토리에 히스토리를 보존하지 않고 병합:

`git merge-repo {{경로/대상/원격_저장소}} {{브랜치_이름}} .`
