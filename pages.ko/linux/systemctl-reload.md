# systemctl reload

> 서비스를 재시작 없이 설정을 다시 로드.
> systemd 유닛 파일이 아니라, 서비스 자체의 설정 (Apache 또는 `nginx` 설정)을 다시 로드하는 것.
> 유닛 파일을 다시 로드하려면, `systemctl daemon-reload` 사용.

- 서비스 설정 다시 로드:

`systemctl reload {{nginx}}`

- 여러 서비스 설정 다시 로드:

`systemctl reload {{유닛1 유닛2 ...}}`

- 현재 사용자 서비스 설정 다시 로드:

`systemctl reload {{pipewire}} --user`
