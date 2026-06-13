# frpc

> 현재 호스트에서 프록시 연결을 시작하려면 `frps`서버에 연결.
> `frp`의 부분.
> 더 많은 정보: <https://github.com/fatedier/frp>.

- 기본 구성 파일(현재 디렉터리의 `frps.ini`로 가정)을 사용하여 서비스를 시작:

`frpc`

- 현재 디렉터리에서 최신 TOML 구성 파일 (`frps.ini` 대신 `frps.toml`)을 사용하여 서비스를 시작:

`frpc {{[-c|--config]}} ./frps.toml`

- 특정 구성 파일을 사용하여, 서비스를 시작:

`frpc {{[-c|--config]}} {{경로/대상/파일}}`

- 구성 파일이 유효한지 확인:

`frpc verify {{[-c|--config]}} {{경로/대상/파일}}`

- Bash, fish, PowerShell 또는 Zsh에 대한 자동 완성 설정 스크립트를 출력:

`frpc completion {{bash|fish|powershell|zsh}}`

- 버전 정보 표시:

`frpc {{[-v|--version]}}`
