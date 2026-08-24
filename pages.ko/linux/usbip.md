# usbip

> 원격으로 USB 장치를 사용합니다.
> 더 많은 정보: <https://manned.org/usbip>.

- 모든 로컬 USB 장치와 해당 버스 ID 나열:

`usbip list {{[-l|--local]}}`

- 서버에서 `usbip` 데몬 시작:

`systemctl start usbipd`

- 서버에서 USB 장치를 `usbip`에 바인드:

`sudo usbip bind {{[-b|--busid]}} {{버스_id}}`

- 클라이언트에서 `usbip`에 필요한 커널 모듈 로드:

`sudo modprobe vhci-hcd`

- 클라이언트에서 `usbip` 장치에 연결(버스 ID는 서버와 동일합니다):

`sudo usbip attach {{[-r|--remote]}} {{ip_주소}} {{[-b|--busid]}} {{버스_id}}`

- 연결된 장치 나열:

`usbip port`

- 장치에서 분리:

`sudo usbip detach {{[-p|--port]}} {{포트}}`

- 장치의 바인드 해제:

`usbip unbind {{[-b|--busid]}} {{버스_id}}`
