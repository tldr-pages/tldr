# nmcli general

> NetworkManager의 일반 설정을 관리합니다.
> 더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#general>.

- NetworkManager의 일반 상태 표시:

`nmcli {{[g|general]}}`

- 현재 장치의 호스트명 표시:

`nmcli {{[g|general]}} {{[h|hostname]}}`

- 현재 장치의 호스트명 변경:

`sudo nmcli {{[g|general]}} {{[h|hostname]}} {{새_호스트명}}`

- NetworkManager의 권한 표시:

`nmcli {{[g|general]}} {{[p|permissions]}}`

- 현재 로깅 수준 및 도메인 표시:

`nmcli {{[g|general]}} {{[l|logging]}}`

- 로깅 수준 및/또는 도메인 설정 (`man NetworkManager.conf`에서 사용 가능한 모든 도메인 확인):

`sudo nmcli {{[g|general]}} {{[l|logging]}} {{[l|level]}} {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{도메인_1,도메인_2,...}}`
