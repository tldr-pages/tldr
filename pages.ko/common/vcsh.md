# vcsh

> Git 저장소를 사용하여 홈 디렉토리를 위한 버전 관리 시스템.
> 같이 보기: `chezmoi`, `stow`, `tuckr`, `homeshick`.
> 더 많은 정보: <https://github.com/RichiH/vcsh>.

- (빈) 저장소 초기화:

`vcsh init {{저장소_이름}}`

- 저장소를 사용자 지정 디렉토리 이름으로 클론:

`vcsh clone {{git_url}} {{저장소_이름}}`

- 관리되는 모든 저장소 나열:

`vcsh list`

- 관리되는 저장소에서 Git 명령 실행:

`vcsh {{저장소_이름}} {{git_명령어}}`

- 모든 관리되는 저장소를 원격으로 푸시/풀:

`vcsh {{push|pull}}`

- 관리되는 저장소에 대한 사용자 지정 `.gitignore` 파일 작성:

`vcsh write-gitignore {{저장소_이름}}`
