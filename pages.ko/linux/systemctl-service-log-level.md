# systemctl service-log-level

> D-Bus를 통해 서비스의 런타임 로그 레벨을 확인하거나 설정.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#service-log-level%20SERVICE%20%5BLEVEL%5D>.

- 서비스의 현재 로그 레벨 출력:

`systemctl service-log-level {{서비스_이름}}`

- 서비스의 로그 레벨 설정 (레벨 이름 대신 0부터 7까지 숫자 사용 가능):

`systemctl service-log-level {{서비스_이름}} {{emerg|alert|crit|err|warning|notice|info|debug}}`
