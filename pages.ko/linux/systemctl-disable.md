# systemctl disable

> systemd 서비스를 비활성화.
> 관련 항목: `systemctl revert`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#disable%20UNIT%E2%80%A6>.

- 부팅 시에 서비스가 실행되지 않도록 설정:

`systemctl disable {{유닛}}`

- 부팅 시 실행되지 않도록 설정하고, 현재 실행 중인 서비스도 중지:

`systemctl disable {{유닛}} --now`

- 사용자 로그인 시 실행되지 않도록 사용자 서비스 비활성화:

`systemctl disable {{유닛}} --user`
