# dhcpig

> 고급 DHCP 자원 고갈 공격 및 스트레스 테스트를 시작.
> DHCPig은 루트 권한으로 실행해야 함.
> 더 많은 정보: <https://github.com/kamorin/DHCPig>.

- 지정된 인터페이스를 사용하여 사용 가능한 DHCP 주소를 소진:

`sudo ./pig.py {{eth0}}`

- eth1 인터페이스를 사용하여 IPv6를 고갈:

`sudo ./pig.py -6 {{eth1}}`

- 인터페이스를 사용하여 퍼지/잘못된 데이터 패킷을 전송:

`sudo ./pig.py --fuzz {{eth1}}`

- 색상 출력 활성화:

`sudo ./pig.py -c {{eth1}}`

- 최소한의 장황함과 색상 출력을 활성화:

`sudo ./pig.py -c --verbosity=1 {{eth1}}`

- 디버그 상세 출력 수준을 100으로 하고 ARP 패킷을 사용해 장치 근처 네트워크를 검색:

`sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp {{eth1}}`

- 임대 정보 출력을 활성화하고, 모든 근처 IP 주소를 검색하고 해제하려 시도:

`sudo ./pig.py --neighbors-scan-arp -r --show-options {{eth1}}`
