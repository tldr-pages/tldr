# airdecap-ng

> WEP, WPA 또는 WPA2로 암호화된 캡처 파일 해독.
> Aircrack-ng 네트워크 소프트웨어 제품군의 일부.
> 더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- 열려있는 네트워크 캡처 파일에서 무선 헤더를 제거, 액세스 포인트의 MAC 주소를 사용해 필터링:

`airdecap-ng -b {{ap_mac}} {{경로/대상/capture.cap}}`

- 16진수 형식의 키를 사용하여 [w]EP 암호화된 캡처 파일을 해독:

`airdecap-ng -w {{hex_key}} {{경로/대상/capture.cap}}`

- 액세스 포인트의 [e]ssid 및 [p]assword를 사용하여 WPA/WPA2 암호화된 캡처 파일을 해독:

`airdecap-ng -e {{essid}} -p {{비밀번호}} {{경로/대상/capture.cap}}`

- 액세스 포인트의 [e]ssid 및 [p]assword를 사용하여 헤더를 보존하는, WPA/WPA2 암호화된 캡처 파일을 해독:

`airdecap-ng -l -e {{essid}} -p {{비밀번호}} {{경로/대상/capture.cap}}`

- 액세스 포인트의 [e]ssid 및 [p]assword를 사용하여 WPA/WPA2 암호화된 캡처 파일을 해독하고, 해당 MAC 주소를 사용하여 필터링:

`airdecap-ng -b {{ap_mac}} -e {{essid}} -p {{비밀번호}} {{경로/대상/capture.cap}}`
