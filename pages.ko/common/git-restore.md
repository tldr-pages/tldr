# git restore

> 작업 트리 파일을 복원합니다. Git 버전 2.23+ 이상이 필요합니다.
> 같이 보기: `git checkout` 및 `git reset`.
> 더 많은 정보: <https://git-scm.com/docs/git-restore>.

- 언스테이지된 파일을 현재 커밋 (HEAD)의 버전으로 복원:

`git restore {{경로/대상/파일}}`

- 언스테이지된 파일을 특정 커밋의 버전으로 복원:

`git restore --source {{커밋}} {{경로/대상/파일}}`

- 추적 중인 파일에 대한 모든 언스테이지된 변경 사항을 폐기:

`git restore :/`

- 파일의 스테이지를 내리기:

`git restore --staged {{경로/대상/파일}}`

- 모든 파일의 스테이지를 내리기:

`git restore --staged :/`

- 스테이지 및 언스테이지된 파일의 모든 변경 사항 폐기:

`git restore --worktree --staged :/`

- 파일의 섹션을 대화적으로 선택하여 복원:

`git restore --patch`
