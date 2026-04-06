# systemctl log-target

> systemd 관리자의 로그 출력 대상을 확인 또는 설정.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#log-target%20%5BTARGET%5D>.

- 현재 systemd 관리자의 로그 대상 출력:

`systemctl log-target`

- 관리자의 로그 출력 대상 설정:

`systemctl log-target {{journal-or-kmsg|journal|kmsg|console|syslog|null|auto}}`
