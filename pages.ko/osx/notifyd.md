# notifyd

> 알림 서버.
> 수동으로 호출하지 않아야 합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/notifyd.8.html>.

- 데몬 시작:

`notifyd`

- 디버그 메시지를 기본 로그 [f]파일(`/var/log/notifyd.log`)로 기록:

`notifyd -d`

- 디버그 메시지를 대체 로그 [f]파일로 기록:

`notifyd -d -log_file {{경로/대상/로그_파일}}`
