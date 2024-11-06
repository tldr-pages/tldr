# netperf

> 네트워크 처리량을 측정하는 벤치마킹 애플리케이션 `netperf`의 클라이언트 측 명령어. `iperf`와 유사합니다.
> 같이 보기: 서버 측 명령어 `netserver`.
> 더 많은 정보: <https://hewlettpackard.github.io/netperf/doc/netperf.html#Global-Command_002dline-Options>.

- 기본 포트(12865)를 통해 특정 IP 주소의 서버에 연결:

`netperf {{주소}}`

- [p]ort 지정:

`netperf {{주소}} -p {{포트}}`

- 샘플링 [l]ength를 초 단위로 지정 (기본값은 10초):

`netperf {{주소}} -l {{초}}`

- IPv[4] 또는 IPv[6] 강제 사용:

`netperf {{주소}} -{{4|6}}`
