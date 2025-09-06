# syncthing

> 지속적인 양방향 분산 폴더 동기화 도구.
> 더 많은 정보: <https://docs.syncthing.net/users/syncthing.html>.

- Syncthing 시작:

`syncthing`

- 웹 브라우저를 열지 않고 Syncthing 시작:

`syncthing --no-browser`

- 홈 디렉토리 변경:

`syncthing --home {{디렉토리/경로}}`

- 로깅을 증가시켜 Syncthing 실행:

`syncthing --verbose`

- 모든 장치 일시 중지:

`syncthing cli config devices pause --all`

- 모든 장치 다시 시작:

`syncthing cli config devices resume --all`

- 웹 인터페이스가 수신 대기하는 주소 변경:

`syncthing --gui-address {{아이피주소:포트|소켓/경로/소켓.sock}}`

- 출력 로그 레벨 설정:

`syncthing --log-level {{정보|경고|오류|디버그}}`
