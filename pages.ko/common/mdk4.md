# mdk4

> IEEE 802.11 프로토콜의 일반적인 취약점을 검증하기 위한 개념 증명(proof-of-concept) 도구.
> 참고: 이 도구는 Wi-Fi 네트워크를 방해하거나 주변 사용자의 연결을 끊을 수 있으므로, 매우 신중하게 사용해야 함.
> 관련 항목: `airodump-ng`, `airmon-ng`.
> 더 많은 정보: <https://github.com/aircrack-ng/mdk4>.

- beacon 프레임을 대량 전송해 가짜 무선 네트워크를 생성 (필요한 경우 `sudo airmon-ng start wifi_interface`를 사용하여 무선 인터페이스를 모니터 모드로 설정):

`sudo mdk4 {{wifi_인터페이스}} b -f {{path/to/beacons.txt}}`

- 모든 BSSID의 모든 클라이언트를 대상으로 연결 해제(deauthentication) 공격 수행:

`sudo mdk4 {{wifi_인터페이스}} d`

- 특정 BSSID를 대상으로 연결 해제(deauthentication) 공격 수행 (`sudo airodump-ng wifi_interface`를 사용하여 사용 가능한 BSSID 목록을 확인):

`sudo mdk4 {{wifi_인터페이스}} d -B {{bssid}}`
