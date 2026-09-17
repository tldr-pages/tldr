# dig

> DNS 조회 유틸리티.
> 관련 항목: `resolvectl`, `nslookup`, `host`.
> 더 많은 정보: <https://manned.org/dig>.

- 호스트이름과 관련된 IP 주소(A 레코드)를 조회하기 :

`dig +short {{example.com}}`

- 지정한 도메인에 대한 상세 응답(A 레코드)을 조회:

`dig +noall +answer {{example.com}}`

- 지정한 도메인 이름에 대해 특정 DNS 레코드 타입을 조회:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- 대체 DNS 서버를 지정하여 조회하고, 필요 시 DNS over TLS(DoT)를 사용:

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- IP 주소에 대해 역방향 DNS 조회(PTR 레코드)를 수행:

`dig -x {{8.8.8.8}}`

- 해당 영역(zone)의 권한 있는 네임서버를 찾고 SOA 레코드를 표시:

`dig +nssearch {{example.com}}`

- 반복 조회(iterative) 조회를 수행하여 도메인 이름을 해석하는 전체 경로를 표시:

`dig +trace {{example.com}}`

- 비표준 포트([p]ort)에서 TCP 프로토콜을 사용하여 DNS 서버에 질의:

`dig +tcp -p {{포트}} @{{dns_서버_ip}} {{example.com}}`
