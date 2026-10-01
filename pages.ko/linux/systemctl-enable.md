# systemctl enable

> systemd 서비스를 활성화.
> 관련 항목: `systemctl revert`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#enable%20UNIT%E2%80%A6>.

- 부팅 시 서비스가 실행되도록 설정:

`systemctl enable {{유닛}}`

- 부팅 시 실행되도록 설정하고, 즉시 서비스 시작:

`systemctl enable {{유닛}} --now`

- 로그인 시 실행되도록 사용자 유닛 활성화:

`systemctl enable {{유닛}} --user`
