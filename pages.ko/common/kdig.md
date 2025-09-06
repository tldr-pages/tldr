# kdig

> 고급 DNS 조회 유틸리티.
> 더 많은 정보: <https://www.knot-dns.cz/docs/latest/html/man_kdig.html>.

- 호스트 이름과 연결된 IP(A 레코드) 조회:

`kdig {{example.com}}`

- 특정 DNS 서버를 지정하여 쿼리(예: Google DNS):

`kdig {{example.com}} @{{8.8.8.8}}`

- 주어진 도메인 이름과 연결된 특정 DNS 레코드 유형 쿼리:

`kdig {{example.com}} {{A|AAAA|NS|SOA|DNSKEY|ANY}}`

- DNS over TLS(DoT)를 사용하여 호스트 이름과 연결된 IP(A 레코드) 조회:

`kdig -d @{{8.8.8.8}} +tls-ca +tls-host={{dns.google}} {{example.com}}`

- DNS over HTTPS(DoH)를 사용하여 호스트 이름과 연결된 IP(A 레코드) 조회:

`kdig -d @{{1.1.1.1}} +https +tls-hostname={{1dot1dot1dot1.cloudflare-dns.com}} {{example.com}}`
