# try-rs

> 대화형 TUI를 사용하여 임시 프로젝트 작업 공간을 관리.
> 더 많은 정보: <https://try-rs.org/#usage>.

- 대화형 TUI 열기:

`try-rs`

- 이름 있는 실험 공간을 생성하거나 해당 작업 공간으로 이동:

`try-rs {{실험공간_이름}}`

- 저장소를 날짜별 폴더에 복제:

`try-rs {{https://github.com/사용자/저장소}}`

- 저장소를 지정한 대상 폴더에 복제:

`try-rs {{https://github.com/사용자/저장소}} {{대상_이름}}`

- 현재 저장소에서 Git Worktree 생성:

`try-rs --worktree {{워크트리_이름}}`

- 지정한 셸을 위한 셸 통합 설정 생성:

`try-rs --setup {{bash|fish|zsh|nu-shell|power-shell}}`
