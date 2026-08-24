# systemctl import-environment

> 쉘의 환경 변수를 systemd 환경으로 가져옴.
> 관련 항목: `systemctl show-environment`, `systemctl unset-environment`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#import-environment%20VARIABLE%E2%80%A6>.

- 변수 하나 가져오기:

`systemctl import-environment {{변수}}`

- 여러 변수 가져오기:

`systemctl import-environment {{변수_1 변수_2 ...}}`

- 사용자 서비스용 환경 변수 가져오기:

`systemctl import-environment {{변수}} --user`
