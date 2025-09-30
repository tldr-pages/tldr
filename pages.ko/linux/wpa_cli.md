# wpa_cli

> wlan 인터페이스를 추가하고 구성.
> 더 많은 정보: <https://manned.org/wpa_cli>.

- 사용 가능한 네트워크 스캔:

`wpa_cli scan`

- 스캔 결과 표시:

`wpa_cli scan_results`

- 네트워크 추가:

`wpa_cli add_network {{번호}}`

- 네트워크의 SSID 설정:

`wpa_cli set_network {{번호}} ssid "{{SSID}}"`

- 네트워크 활성화:

`wpa_cli enable_network {{번호}}`

- 구성 저장:

`wpa_cli save_config`
