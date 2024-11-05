# nping

> 네트워크 패킷 생성 도구/핑 유틸리티.
> 더 많은 정보: <https://nmap.org/nping/>.

- 사용자가 허용된 경우 ICMP를 사용하여 지정된 호스트에 핑, 그렇지 않으면 TCP 사용:

`nping {{example.com}}`

- 사용자가 허용된 경우 ICMP를 사용하여 지정된 호스트에 핑:

`nping --icmp --privileged {{example.com}}`

- UDP를 사용하여 지정된 호스트에 핑:

`nping --udp {{example.com}}`

- 지정된 포트에서 TCP를 사용하여 지정된 호스트에 핑:

`nping --tcp --dest-port {{443}} {{example.com}}`

- 특정 횟수만큼 핑:

`nping --count {{10}} {{example.com}}`

- 각 핑 사이에 일정 시간 대기:

`nping --delay {{5s}} {{example.com}}`

- 지정된 인터페이스를 통해 요청 전송:

`nping --interface {{eth0}} {{example.com}}`

- IP 범위에 핑:

`nping {{10.0.0.1-10}}`
