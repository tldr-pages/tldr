# create_ap

> 모든 채널에서 AP(액세스 포인트)를 생성합니다.
> 더 많은 정보: <https://github.com/oblique/create_ap>.

- 암호 없이 열린 네트워크 생성:

`create_ap {{wlan0}} {{eth0}} {{액세스_포인트_SSID}}`

- WPA + WPA2 암호 사용:

`create_ap {{wlan0}} {{eth0}} {{액세스_포인트_SSID}} {{암호}}`

- 인터넷 공유 없이 액세스 포인트 생성:

`create_ap -n {{wlan0}} {{액세스_포인트_SSID}} {{암호}}`

- 인터넷 공유가 가능한 브리지 네트워크 생성:

`create_ap -m bridge {{wlan0}} {{eth0}} {{액세스_포인트_SSID}} {{암호}}`

- 사전 구성된 브리지 인터페이스를 사용하는 인터넷 공유 브리지 네트워크 생성:

`create_ap -m bridge {{wlan0}} {{br0}} {{액세스_포인트_SSID}} {{암호}}`

- 동일한 Wi-Fi 인터페이스에서 인터넷 공유를 위한 액세스 포트 생성:

`create_ap {{wlan0}} {{wlan0}} {{액세스_포인트_SSID}} {{암호}}`

- 다른 Wi-Fi 어댑터 드라이버 선택:

`create_ap --driver {{wifi_adapter}} {{wlan0}} {{eth0}} {{액세스_포인트_SSID}} {{암호}}`
