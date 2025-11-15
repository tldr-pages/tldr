# git stash

> 로컬 Git 변경사항을 임시 영역에 저장합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-stash>.

- 새롭게 생성한 (Git에서 관리하지 않는) 파일을 제외하고 현재 변경사항을 메시지와 함께 임시 저장:

`git stash push {{[-m|--message]}} {{optional_stash_message}}`

- 새롭게 생성한 (Git에서 관리하지 않는) 파일을 포함하여 현재 변경사항을 임시 저장:

`git stash {{[-u|--include-untracked]}}`

- 변경된 파일들의 특정 부분만 선택하여 임시 저장 (대화형 프롬프트):

`git stash {{[-p|--patch]}}`

- 모든 임시 저장 목록 표시 (임시 저장 이름, 관련 브랜치 및 메시지 표시):

`git stash list`

- 임시 저장(기본값은 `stash@{0}`)과 해당 임시 저장이 생성된 시점의 커밋 사이의 변경 사항을 터미널에 상세히 표시:

`git stash show {{[-p|--patch]}} {{stash@{0}}}`

- 임시 저장 적용 (기본값은 가장 최근 임시 저장인 stash@{0}):

`git stash apply {{optional_stash_name_or_commit}}`

- 임시 저장을 적용하고 (기본값은 stash@{0}), 적용 시 충돌이 없으면 임시 저장 목록에서 제거:

`git stash pop {{optional_stash_name}}`

- 모든 임시 저장 삭제:

`git stash clear`
