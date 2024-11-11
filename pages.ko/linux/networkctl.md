# networkctl

> 네트워크 링크의 상태를 조회합니다.
> `systemd-networkd`를 사용하여 네트워크 구성을 관리합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- 기존 링크와 그 상태를 나열:

`networkctl list`

- 전체 네트워크 상태 표시:

`networkctl status`

- 네트워크 장치를 활성화:

`networkctl up {{인터페이스1 인터페이스2 ...}}`

- 네트워크 장치를 비활성화:

`networkctl down {{인터페이스1 인터페이스2 ...}}`

- 동적 구성 갱신 (예: DHCP 서버로부터 받은 IP 주소):

`networkctl renew {{인터페이스1 인터페이스2 ...}}`

- 구성 파일(.netdev 및 .network) 재로드:

`networkctl reload`

- 네트워크 인터페이스 재구성 (구성을 편집한 경우, 먼저 `networkctl reload`를 호출해야 함):

`networkctl reconfigure {{인터페이스1 인터페이스2 ...}}`
