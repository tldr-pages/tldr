# tftp

> Trivial File Transfer Protocol 클라이언트.
> 더 많은 정보: <https://manned.org/tftp.1>.

- TFTP 서버의 IP 주소와 포트를 지정하여 연결:

`tftp {{서버_IP}} {{포트}}`

- TFTP 서버에 연결하고 TFTP [c]명령 실행:

`tftp {{서버_IP}} -c {{명령}}`

- IPv6를 사용하여 TFTP 서버에 연결하고 시작 포트를 [R]범위 내로 강제 설정:

`tftp {{서버_IP}} -6 -R {{포트}}:{{포트}}`

- tftp 클라이언트를 통해 전송 모드를 바이너리 또는 ASCII로 설정:

`mode {{binary|ascii}}`

- tftp 클라이언트를 통해 서버로부터 파일 다운로드:

`get {{파일}}`

- tftp 클라이언트를 통해 서버로 파일 업로드:

`put {{파일}}`

- tftp 클라이언트 종료:

`quit`
