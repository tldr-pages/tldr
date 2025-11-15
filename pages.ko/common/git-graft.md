# git graft

> 브랜치의 커밋들을 다른 브랜치로 병합하고, 소스 브랜치를 삭제.
> `git-extras`의 일부.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- 소스 브랜치의 모든 커밋을 대상 브랜치로 병합하고, 소스 브랜치를 삭제:

`git graft {{source_branch}} {{target_branch}}`
