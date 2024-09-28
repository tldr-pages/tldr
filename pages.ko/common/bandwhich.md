# bandwhich

> 프로세스, 연결 또는 원격 IP/호스트 이름별로 현재 네트워크 사용량을 표시.
> 더 많은 정보: <https://github.com/imsnif/bandwhich>.

- 원격 주소 테이블만 표시:

`bandwhich --addresses`

- DNS 쿼리 표시:

`bandwhich --show-dns`

- 총 (누적) 사용량 표시:

`bandwhich --total-utilization`

- 특정 네트워크 인터페이스에 대한 네트워크 활용도를 표시:

`bandwhich --interface {{eth0}}`

- 특정 DNS 서버로 DNS 쿼리를 표시:

`bandwhich --show-dns --dns-server {{dns_서버_ip}}`
