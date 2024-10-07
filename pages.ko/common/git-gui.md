# git gui

> Git의 GUI를 사용하여 브랜치, 커밋, 원격 저장소를 관리하고 로컬 병합을 수행할 수 있습니다.
> 같이 보기: `git-cola`, `gitk`.
> 더 많은 정보: <https://git-scm.com/docs/git-gui>.

- GUI 시작:

`git gui`

- 각 줄에 작성자 이름과 커밋 해시가 표시된 특정 파일 보기:

`git gui blame {{경로/대상/파일}}`

- 특정 리비전에서 `git gui blame` 열기:

`git gui blame {{리비전}} {{경로/대상/파일}}`

- 특정 줄을 중심으로 뷰를 스크롤하여 `git gui blame` 열기:

`git gui blame --line={{줄}} {{경로/대상/파일}}`

- 하나의 커밋을 만들기 위한 창을 열고 완료되면 쉘로 돌아가기:

`git gui citool`

- "마지막 커밋 수정" 모드로 `git gui citool` 열기:

`git gui citool --amend`

- 읽기 전용 모드로 `git gui citool` 열기:

`git gui citool --nocommit`

- 특정 브랜치의 트리 브라우저를 열고, 파일을 클릭하면 블레임 도구 열기:

`git gui browser maint`
