# git cherry-pick

> 기존의 커밋에서 가져온 변경내용을 현재 브랜치에 적용합니다.
> 변경내용을 다른 브랜치에 적용하고싶으면, 우선 `git checkout`을 사용해 원하는 브랜치로 변경하세요.
> 더 많은 정보: <https://git-scm.com/docs/git-cherry-pick>.

- 커밋을 현재 브랜치에 적용:

`git cherry-pick {{커밋}}`

- 특정 범위의 커밋들을 현재 브랜치에 적용 (`git rebase --onto`도 보세요):

`git cherry-pick {{시작_커밋}}~..{{끝_커밋}}`

- 연속되지 않은 여러 커밋들을 현재 브랜치에 적용:

`git cherry-pick {{커밋_1}} {{커밋_2}}`

- 커밋의 변경내역을 커밋 없이 디렉토리에 추가:

`git cherry-pick -n {{커밋}}`
