# dbus-daemon

> 여러 프로그램이 메시지를 교환할 수 있도록 하는 D-Bus 메시지 데몬.
> 더 많은 정보: <https://dbus.freedesktop.org/doc/dbus-daemon.1.html>.

- 구성 파일을 사용하여 데몬 실행:

`dbus-daemon --config-file {{경로/대상/파일}}`

- 표준 로그인 세션당 메시지 버스 구성으로 데몬 실행:

`dbus-daemon --session`

- 표준 시스템 전체 메시지 버스 구성으로 데몬 실행:

`dbus-daemon --system`

- 수신할 주소 설정 및 해당 구성 값 재정의:

`dbus-daemon --address {{주소}}`

- 프로세스 ID를 `stdout`에 출력:

`dbus-daemon --print-pid`

- 메시지를 시스템 로그에 기록하도록 메시지 버스를 강제 설정:

`dbus-daemon --syslog`
