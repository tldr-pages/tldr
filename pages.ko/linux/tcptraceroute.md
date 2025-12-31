# tcptraceroute

> TCP 패킷을 사용하는 traceroute 구현.
> 더 많은 정보: <https://manned.org/tcptraceroute>.

- 호스트까지의 경로 추적:

`tcptraceroute {{호스트}}`

- 목적지 포트와 패킷 길이(바이트 단위) 지정:

`tcptraceroute {{호스트}} {{목적지_포트}} {{패킷_길이}}`

- 로컬 소스 포트와 소스 주소 지정:

`tcptraceroute {{호스트}} -p {{소스_포트}} -s {{소스_주소}}`

- 첫 번째 및 최대 TTL 설정:

`tcptraceroute {{호스트}} -f {{첫번째_ttl}} -m {{최대_ttl}}`

- 대기 시간과 홉당 쿼리 수 지정:

`tcptraceroute {{호스트}} -w {{대기_시간}} -q {{쿼리_수}}`

- 인터페이스 지정:

`tcptraceroute {{호스트}} -i {{인터페이스}}`
