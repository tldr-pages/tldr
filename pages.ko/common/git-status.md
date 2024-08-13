# git status

> Git 저장소의 파일 변경 사항을 표시합니다.
> 현재 체크아웃된 커밋과 비교하여 변경된, 추가된 및 삭제된 파일을 나열합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-status>.

- 커밋할 파일로 아직 추가되지 않은 변경된 파일 보기:

`git status`

- [s]hort 형식으로 출력:

`git status --short`

- [b]ranch 및 추적 정보 표시:

`git status --branch`

- [s]hort 형식으로 출력하면서 [b]ranch 정보 표시:

`git status --short --branch`

- 현재 숨겨둔 엔트리의 수 표시:

`git status --show-stash`

- 출력에 추적되지 않는 파일을 표시하지 않기:

`git status --untracked-files=no`
