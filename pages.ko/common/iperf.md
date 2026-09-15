# iperf

> 컴퓨터 간 네트워크 대역폭을 측정하는 도구.
> 더 많은 정보: <https://iperf.fr/iperf-doc.php>.

- 서버 모드로 실행:

`iperf {{[-s|--server]}}`

- UDP 모드로 서버 실행 및 포트 5001에서 대기:

`iperf {{[-u|--udp]}} {{[-s|--server]}} {{[-p|--port]}} {{5001}}`

- 클라이언트 모드로 실행:

`iperf {{[-c|--client]}} {{서버_주소}}`

- 2초 간격으로 클라이언트 실행:

`iperf {{[-c|--client]}} {{서버_주소}} {{[-i|--interval]}} {{2}}`

- 5개의 병렬 스레드로 클라이언트 실행:

`iperf {{[-c|--client]}} {{서버_주소}} {{[-P|--parallel]}} {{5}}`

- UDP 모드로 클라이언트 실행:

`iperf {{[-u|--udp]}} {{[-c|--client]}} {{서버_주소}} {{[-p|--port]}} {{5001}}`
