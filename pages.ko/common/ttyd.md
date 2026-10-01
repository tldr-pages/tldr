# ttyd

> 터미널 또는 임의의 명령을 웹을 통해 공유.
> 더 많은 정보: <https://github.com/tsl0922/ttyd#command-line-options>.

- 기본 포트 (7681)에서 Bash 쉘을 읽기 전용으로 공유 하는 웹 서버 시작:

`ttyd bash`

- 지정한 포트에서 Bash 쉘 시작:

`ttyd {{[-p|--port]}} {{8080}} bash`

- 클라이언트가 터미널에 입력할 수 있도록 허용:

`ttyd {{[-W|--writable]}} {{명령어}}`

- 클라이언트 옵션 설정:

`ttyd {{[-t|--client-option]}} {{key=value}} {{명령어}}`

- 도움말 표시:

`ttyd {{[-h|--help]}}`

- 버전 정보 표시:

`ttyd {{[-v|--version]}}`
