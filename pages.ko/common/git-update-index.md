# git update-index

> Git 색인을 조작하기 위한 명령어.
> 더 많은 정보: <https://git-scm.com/docs/git-update-index>.

- 수정된 파일이 변경되지 않은 것처럼 가장하기 (`git status`에서 변경 사항으로 표시되지 않음):

`git update-index --skip-worktree {{경로/대상/수정된_파일}}`
