# systemctl unset-environment

> 하나 이상의 서비스 매니저 환경 변수를 제거.
> `systemctl set-environment 효과를 되돌림`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#unset-environment%20VARIABLE%E2%80%A6>.

- 단일 환경 변수 제거:

`systemctl unset-environment {{변수}}`

- 여러 환경 변수 한 번에 제거:

`systemctl unset-environment {{변수1 변수2 ...}}`

- 사용자 서비스 매니저의 환경 변수 제거:

`systemctl unset-environment {{변수}} --user`
