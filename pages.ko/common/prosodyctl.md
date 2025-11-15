# prosodyctl

> Prosody XMPP 서버의 제어 도구.
> 참고: `prosodyctl`을 통한 프로세스 관리는 권장되지 않습니다. 대신, 시스템에서 제공하는 도구(예: `systemctl`)를 사용하세요.
> 더 많은 정보: <https://prosody.im/doc/prosodyctl>.

- Prosody 서버의 상태 표시:

`sudo prosodyctl status`

- 서버의 구성 파일 다시 로드:

`sudo prosodyctl reload`

- Prosody XMPP 서버에 사용자 추가:

`sudo prosodyctl adduser {{user@example.com}}`

- 사용자의 비밀번호 설정:

`sudo prosodyctl passwd {{user@example.com}}`

- 사용자를 영구적으로 삭제:

`sudo prosodyctl deluser {{user@example.com}}`
