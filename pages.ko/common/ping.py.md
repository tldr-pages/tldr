# ping.py

> ICMP를 사용해 IPv4 호스트에 접근 가능한지 확인.
> ICMP echo 요청을 전송하고 echo 응답을 수신.
> 참고: raw 소켓 접근을 위해선 root 권한이 필요합니다 (예: `sudo`로 실행).
> Impacket 도구 모음 중 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 지정한 소스 IPv4 주소에서 호스트로 ping을 전송:

`ping.py {{소스_ipv4}} {{목적지_ipv4}}`

- 192.168.1.10에서 192.168.1.100으로 ping을 전송:

`ping.py 192.168.1.10 192.168.1.100`
