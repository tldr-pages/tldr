# aircrack-ng

> 수집된 패킷의 핸드셰이크 과정 중, WEP 및 WPA/WPA2 키를 크랙.
> Aircrack-ng 네트워크 소프트웨어 제품군의 일부.
> 더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- [w]ordlist를 사용해 캡처 파일에서 크랙 키를 생성:

`aircrack-ng -w {{경로/대상/wordlist.txt}} {{경로/대상/capture.cap}}`

- [w]ordlist와 액세스 포인트의 [e]ssid를 사용하여 캡처 파일에서 키를 크랙:

`aircrack-ng -w {{경로/대상/wordlist.txt}} -e {{essid}} {{경로/대상/capture.cap}}`

- [w]ordlist와 액세스 포인트의 MAC 주소를 사용하여 캡처 파일에서 키를 크랙:

`aircrack-ng -w {{경로/대상/wordlist.txt}} --bssid {{mac}} {{경로/대상/capture.cap}}`
