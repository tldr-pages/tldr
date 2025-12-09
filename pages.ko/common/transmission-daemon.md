# transmission-daemon

> `transmission-remote` 또는 웹 인터페이스로 제어되는 데몬.
> 같이 보기: `transmission`.
> 더 많은 정보: <https://manned.org/transmission-daemon>.

- 헤드리스 `transmission` 세션 시작:

`transmission-daemon`

- 특정 디렉터리를 감시하여 새로운 토렌트를 시작:

`transmission-daemon {{[-c|--watch-dir]}} {{경로/대상/폴더}}`

- JSON 형식으로 데몬 설정 덤프:

`transmission-daemon --dump-settings > {{경로/대상/파일.json}}`

- 웹 인터페이스에 대한 특정 설정으로 시작:

`transmission-daemon {{[-t|--auth]}} {{[-u|--username]}} {{사용자명}} {{[-v|--password]}} {{비밀번호}} {{[-p|--port]}} {{9091}} {{[-a|--allowed]}} {{127.0.0.1}}`
