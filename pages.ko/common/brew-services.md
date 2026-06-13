# brew services

> macOS에서는 `launchctl`, Linux에서는 `systemctl`을 사용하여 백그라운드 서비스를 관리.
> 더 많은 정보: <https://docs.brew.sh/Manpage#services-subcommand>.

- 현재 사용자 기준으로 관리 중인 모든 서비스 목록 출력:

`brew services`

- 모든 서비스에 대한 상세 정보 출력:

`brew services info --all`

- 서비스를 즉시 시작하고 로그인 (또는 부팅) 시 자동 실행 등록:

`brew services start {{패키지}}`

- 서비스를 즉시 중지하고 로그인 (또는 부팅) 시 자동 실행 해제:

`brew services stop {{패키지}}`

- 서비스 재시작 후 로그인 시 자동 실행 등록:

`brew services restart {{패키지}}`

- 사용하지 않는 서비스 정리:

`brew services cleanup`
