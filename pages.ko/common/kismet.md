# kismet

> 무선 네트워크 및 장치 감지기, 스니퍼, 워드라이빙 도구, WIDS(무선 침입 탐지) 프레임워크.
> 더 많은 정보: <https://www.kismetwireless.net/docs/readme/starting/commandline/>.

- 특정 무선 인터페이스에서 패킷 캡처:

`sudo kismet -c {{wlan0}}`

- 무선 인터페이스에서 여러 채널 모니터링:

`sudo kismet -c {{wlan0,wlan1}} -m`

- 패킷을 캡처하고 특정 디렉토리에 저장:

`sudo kismet -c {{wlan0}} -d {{경로/대상/출력}}`

- 특정 구성 파일로 Kismet 시작:

`sudo kismet -c {{wlan0}} -f {{경로/대상/config.conf}}`

- SQLite 데이터베이스에 데이터를 모니터링하고 기록:

`sudo kismet -c {{wlan0}} --log-to-db`

- 특정 데이터 소스를 사용하여 모니터링:

`sudo kismet -c {{wlan0}} --data-source={{rtl433}}`

- 특정 이벤트에 대한 경고 활성화:

`sudo kismet -c {{wlan0}} --enable-alert={{new_ap}}`

- 특정 AP의 패킷에 대한 자세한 정보 표시:

`sudo kismet -c {{wlan0}} --info {{BSSID}}`
