# update-rc.d

> System-V 스타일의 init 스크립트 링크를 설치하고 제거합니다.
> Init 스크립트는 `/etc/init.d/`에 있습니다.
> 더 많은 정보: <https://manned.org/update-rc.d>.

- 서비스 설치:

`update-rc.d {{mysql}} defaults`

- 서비스 활성화:

`update-rc.d {{mysql}} enable`

- 서비스 비활성화:

`update-rc.d {{mysql}} disable`

- 서비스를 강제로 제거:

`update-rc.d -f {{mysql}} remove`
