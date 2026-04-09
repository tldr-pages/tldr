# systemctl log-level

> systemd 관리자의 로그 레벨 확인 또는 설정.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#log-level%20%5BLEVEL%5D>.

- 현재 systemd 관리자의 로그 수준 출력:

`systemctl log-level`

- 관리자 로그 수준을 설정:

`systemctl log-level {{emerg|alert|crit|err|warning|notice|info|debug}}`
