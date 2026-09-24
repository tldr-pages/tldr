# systemctl set-default

> `default.target` 별칭을 지정한 타겟 유닛으로 연결.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-default%20TARGET>.

- `systemd`의 기본 부팅 모드 설정:

`systemctl set-default {{target_name.target}}`

- 기본적으로 GUI 모드로 부팅하도록 `systemd` 설정:

`systemctl set-default graphical.target`

- 기본적으로 CLI 모드로 부팅하도록 `systemd` 설정:

`systemctl set-default multi-user.target`
