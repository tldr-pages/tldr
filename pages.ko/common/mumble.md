# mumble

> 저지연, 고품질 음성 채팅 소프트웨어.
> 더 많은 정보: <https://manned.org/mumble>.

- Mumble 열기:

`mumble`

- Mumble을 열고 즉시 서버에 연결:

`mumble mumble://{{사용자이름}}@{{예제.com}}`

- Mumble을 열고 즉시 비밀번호로 보호된 서버에 연결:

`mumble mumble://{{사용자이름}}:{{비밀번호}}@{{예제.com}}`

- 실행 중인 Mumble 인스턴스에서 마이크 음소거/음소거 해제:

`mumble rpc {{mute|unmute}}`

- Mumble의 마이크 및 오디오 출력 음소거/음소거 해제:

`mumble rpc {{deaf|undeaf}}`
