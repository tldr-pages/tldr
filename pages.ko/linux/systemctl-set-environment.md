# systemctl set-environment

> 하나 이상의 서비스 매니저 환경 변수를 설정.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-environment%20VARIABLE=VALUE%E2%80%A6>.

- 단일 환경 변수 설정:

`systemctl set-environment {{var value}}`

- 여러 환경 변수 한 번에 설정:

`systemctl set-environment {{var1 value1 var2 value2 ...}}`

- 사용자 서비스 매니저용 환경 변수 설정:

`systemctl set-environment {{var value}} --user`
