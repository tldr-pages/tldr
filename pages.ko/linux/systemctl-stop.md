# systemctl stop

> systemd 유닛을 중지.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#stop%20PATTERN%E2%80%A6>.

- 유닛 중지:

`systemctl stop {{유닛}}`

- 경고 메시지 없이 서비스 중지:

`systemctl stop {{유닛}} --no-warn`

- 사용자 유닛 중지:

`systemctl stop {{유닛}} --user`
