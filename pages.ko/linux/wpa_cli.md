# wpa_cli

> wlan 인터페이스를 추가하고 구성.
> 더 많은 정보: <https://manned.org/wpa_cli>.

- 사용 가능한 네트워크 스캔:

`sudo wpa_cli scan`

- 스캔 결과 표시:

`sudo wpa_cli scan_results`

- 네트워크 추가:

`sudo wpa_cli {{[add_n|add_network]}} {{번호}}`

- 네트워크의 SSID 설정:

`sudo wpa_cli {{[set_n|set_network]}} {{번호}} ssid "{{SSID}}"`

- 네트워크 활성화:

`sudo wpa_cli {{[en|enable_network]}} {{번호}}`

- 구성 저장:

`sudo wpa_cli {{[sa|save_config]}}`
