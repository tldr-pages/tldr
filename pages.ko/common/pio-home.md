# pio home

> PlatformIO Home 웹 서버 시작.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- 기본 웹 브라우저에서 PlatformIO Home 열기:

`pio home`

- 특정 HTTP 포트 사용 (기본값은 8008):

`pio home --port {{포트}}`

- 특정 IP 주소에 바인딩 (기본값은 127.0.0.1):

`pio home --host {{ip_주소}}`

- 기본 웹 브라우저에서 PlatformIO Home을 자동으로 열지 않음:

`pio home --no-open`

- 클라이언트가 연결되어 있지 않을 때 타임아웃(초) 후 서버 자동 종료:

`pio home --shutdown-timeout {{시간}}`

- 고유한 세션 식별자를 지정하여 PlatformIO Home을 다른 인스턴스와 격리하고 제3자 접근으로부터 보호:

`pio home --session-id {{세션_아이디}}`
