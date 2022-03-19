# arping

> ARP 프로토콜을 사용하여 네트워크에서 호스트를 발견하고 탐색합니다.
> MAC 주소 검색에 유용합니다.
> 더 많은 정보: <https://github.com/ThomasHabets/arping>.

- ARP 요청 패킷으로 호스트 ping 하기:

`arping {{host_ip}}`

- 특정 인터페이스의 호스트로 ping 하기:

`arping -I {{interface}} {{host_ip}}`

- 첫 응답을 한 호스트로 ping 하기:

`arping -f {{host_ip}}`

- 호스트에 특정 횟수 ping 하기:

`arping -c {{count}} {{host_ip}}`

- 브로드캐스트 ARP 요청 패킷을 통해 이웃 ARP 캐시 업데이트:

`arping -U {{ip_to_broadcast}}`

- 3초의 시간 제한을 사용하여 ARP 요청을 전송하여 네트워크에서 중복된 IP 주소를 탐지합니다:

`arping -D -w {{3}} {{ip_to_check}}`
