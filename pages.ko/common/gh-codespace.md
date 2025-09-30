# gh codespace

> GitHub에서 코드스페이스를 연결하고 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_codespace>.

- GitHub에서 코드스페이스를 대화식으로 생성:

`gh {{[cs|codespace]}} create`

- 사용 가능한 모든 코드스페이스 나열:

`gh {{[cs|codespace]}} {{[ls|list]}}`

- SSH를 통해 코드스페이스에 대화식으로 연결:

`gh {{[cs|codespace]}} ssh`

- 특정 파일을 코드스페이스로 대화식으로 전송:

`gh {{[cs|codespace]}} cp {{경로/대상/소스_파일}} remote:{{경로/대상/원격_파일}}`

- 코드스페이스의 포트를 대화식으로 나열:

`gh {{[cs|codespace]}} ports`

- 코드스페이스의 로그를 대화식으로 표시:

`gh {{[cs|codespace]}} logs`

- 코드스페이스를 대화식으로 삭제:

`gh {{[cs|codespace]}} delete`

- 하위 명령어에 대한 도움말 표시:

`gh {{[cs|codespace]}} {{code|cp|create|delete|edit|...}} {{[-h|--help]}}`
