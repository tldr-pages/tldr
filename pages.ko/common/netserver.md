# netserver

> 네트워크 처리량을 측정하는 벤치마킹 애플리케이션 `netperf`의 서버 측 명령.
> 같이 보기: `netperf`, 클라이언트 측 명령.
> 더 많은 정보: <https://manned.org/netserver.1>.

- 기본 포트(12865)에서 서버 시작 및 백그라운드로 포크:

`netserver`

- 포그라운드에서 서버 시작 및 포크하지 않음:

`netserver -D`

- 포트 지정:

`netserver -p {{포트}}`

- IPv[4] 또는 IPv[6] 강제 설정:

`netserver -{{4|6}}`
