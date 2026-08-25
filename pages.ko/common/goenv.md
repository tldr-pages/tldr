# goenv

> Golang 버전을 설치, 제거 또는 전환하는 도구.
> "1.16.15", "1.22.8" 등과 같은 버전 번호 지원.
> 더 많은 정보: <https://github.com/go-nv/goenv>.

- 사용 가능한 모든 goenv 명령 목록 표시:

`goenv commands`

- 특정 Golang 버전 설치:

`goenv install {{go_버전}}`

- 현재 프로젝트에서 특정 Golang 버전 사용:

`goenv local {{go_버전}}`

- 기본 Golang 버전 설정:

`goenv global {{go_버전}}`

- 사용 가능한 모든 Golang 버전 목록 표시 및 기본 버전 강조 표시:

`goenv versions`

- 지정한 Go 버전 제거:

`goenv uninstall {{go_버전}}`

- 선택한 Go 버전으로 실행파일 실행:

`goenv exec go run {{go_버전}}`
