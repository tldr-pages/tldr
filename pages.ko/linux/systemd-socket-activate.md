# systemd-socket-activate

> systemd 서비스의 소켓 활성화.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-socket-activate.html>.

- 특정 소켓이 연결되었을 때 서비스를 활성화:

`systemd-socket-activate {{경로/대상/socket.service}}`

- 서비스에 대해 여러 소켓을 활성화:

`systemd-socket-activate {{경로/대상/socket1.service}} {{경로/대상/socket2.service}}`

- 활성화되는 서비스에 환경 변수를 전달:

`{{SYSTEMD_SOCKET_ACTIVATION=1}} systemd-socket-activate {{경로/대상/socket.service}}`

- 알림 소켓과 함께 서비스를 활성화:

`systemd-socket-activate {{경로/대상/socket.socket}} {{경로/대상/service.service}}`

- 지정된 포트로 서비스를 활성화:

`systemd-socket-activate {{경로/대상/socket.service}} -l {{8080}}`
