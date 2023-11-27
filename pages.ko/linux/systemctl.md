# systemctl

> systemd 시스템 및 서비스 관리자를 제어합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- 실행 중인 서비스 모두 표시:

`systemctl status`

- 실패한 장치를 나열:

`systemctl --failed`

- 서비스 시작/중지/다시 시작/다시 로드:

`systemctl {{start|stop|restart|reload}} {{장치}}`

- 장치 상태 표시:

`systemctl status {{장치}}`

- 부팅 시 시작될 장치를 활성화/비활성화:

`systemctl {{enable|disable}} {{장치}}`

- 자동 및 수동 활성화를 방지하기 위해 장치 마스크/마스크 해제:

`systemctl {{mask|unmask}} {{장치}}`

- systemd를 다시 로드하고, 새 장치 또는 변경된 장치를 검색:

`systemctl daemon-reload`

- 장치가 활성화되어 있는지 확인:

`systemctl is-enabled {{장치}}`
