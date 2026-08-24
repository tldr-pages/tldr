# ip

> IP 설정 관리.
> 설정 모드에서 사용함.
> 더 많은 정보: <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book.html>.

- SSH 버전 설정:

`ip ssh version {{2}}`

- 장치의 IP 주소 설정 (`interface 명령` 내부에서 실행):

`ip address {{10.0.0.1}} {{255.255.255.0}}`

- DHCP로 IP 주소 자동 할당 설정 (`interface 명령` 내부에서 실행):

`ip address dhcp`

- 도메인 이름 설정:

`ip domain-name {{example.com}}`
