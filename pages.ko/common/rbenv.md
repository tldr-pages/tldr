# rbenv

> 쉽게 Ruby 버전을 설치하고 애플리케이션 환경을 관리.
> 같이 보기: `asdf`.
> 더 많은 정보: <https://github.com/rbenv/rbenv>.

- Ruby 버전 설치:

`rbenv install {{버전}}`

- 각 Ruby의 최신 안정 버전 목록 표시:

`rbenv install --list`

- 설치된 Ruby 버전 목록 표시:

`rbenv versions`

- 시스템 전체에서 특정 Ruby 버전 사용:

`rbenv global {{버전}}`

- 애플리케이션/프로젝트 디렉토리에 특정 Ruby 버전 사용:

`rbenv local {{버전}}`

- 현재 선택된 Ruby 버전 표시:

`rbenv version`

- Ruby 버전 제거:

`rbenv uninstall {{버전}}`

- 지정된 실행 파일을 포함하는 모든 Ruby 버전 표시:

`rbenv whence {{실행_파일}}`
