# tuckr

> Rust로 작성된 도트파일 관리 도구.
> 같이 보기: `chezmoi`, `vcsh`, `homeshick`, `stow`.
> 더 많은 정보: <https://github.com/RaphGL/Tuckr>.

- 도트파일 상태 확인:

`tuckr status`

- 모든 도트파일 시스템에 추가:

`tuckr add \*`

- 지정된 프로그램을 제외한 모든 도트파일 추가:

`tuckr add \* -e {{프로그램1}},{{프로그램2}}`

- 시스템에서 모든 도트파일 제거:

`tuckr rm \*`

- 프로그램 도트파일 추가 및 설정 스크립트 실행:

`tuckr set {{프로그램}}`
