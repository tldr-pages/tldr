# ping6.py

> ICMPv6를 사용해 IPv6 호스트에 접근 가능한지 확인.
> ICMPv6 echo 요청을 전송하고 echo 응답을 수신.
> 참고: raw 소켓 접근을 위해선 root 권한이 필요합니다 (예: `sudo`로 실행).
> Impacket 도구 모음 중 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 지정한 소스 IPv6 주소에서 IPv6 호스트로 ping을 전송:

`ping6.py {{소스_ipv6}} {{목적지_ipv6}}`

- 2001:db8::1에서 2001:db8::2로 ping을 전송:

`ping6.py 2001:db8::1 2001:db8::2`
