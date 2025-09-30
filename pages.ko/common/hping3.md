# hping3

> TCP, UDP 및 원시 IP와 같은 프로토콜을 지원하는 고급 ping 유틸리티.
> 높은 권한으로 실행하는 것이 가장 좋음.
> 더 많은 정보: <https://github.com/antirez/hping>.

- 4개의 ICMP ping 요청으로 대상에 ping을 보냄:

`hping3 --icmp --count {{4}} {{ip_또는_호스트명}}`

- 포트 80에서 UDP를 통해 IP 주소를 ping:

`hping3 --udp --destport {{80}} --syn {{ip_또는_호스트명}}`

- 특정 로컬 소스 포트 5090에서 스캔해 TCP 포트 80을 스캔:

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_또는_호스트명}}`

- 특정 대상 포트에 대한 TCP 스캔을 사용해 경로를 추적:

`hping3 --traceroute --verbose --syn --destport {{80}} {{ip_또는_호스트명}}`

- 특정 IP 주소에서 TCP 포트 세트를 스캔 :

`hping3 --scan {{80,3000,9000}} --syn {{ip_또는_호스트명}}`

- TCP ACK 스캔을 수행해, 특정 호스트가 살아 있는지 확인:

`hping3 --count {{2}} --verbose --destport {{80}} --ack {{ip_또는_호스트명}}`

- 포트 80에서 부하 테스트를 수행:

`hping3 --flood --destport {{80}} --syn {{ip_또는_호스트명}}`
