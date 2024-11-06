# syncthing

> 지속적인 양방향 분산 폴더 동기화 도구.
> 더 많은 정보: <https://docs.syncthing.net/>.

- Syncthing 시작:

`syncthing`

- 웹 브라우저를 열지 않고 Syncthing 시작:

`syncthing -no-browser`

- 장치 ID 출력:

`syncthing -device-id`

- 홈 디렉토리 변경:

`syncthing -home={{경로/대상/폴더}}`

- 전체 색인 교환 강제 수행:

`syncthing -reset-deltas`

- 웹 인터페이스가 수신 대기할 주소 변경:

`syncthing -gui-address={{IP_주소:포트|경로/대상/socket.sock}}`

- Syncthing이 사용하는 파일 경로 표시:

`syncthing -paths`

- Syncthing 모니터 프로세스 비활성화:

`syncthing -no-restart`
