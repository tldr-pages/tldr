# dog

> DNS 조회 유틸리티.
> 다채로운 출력을 제공하고, DNS-over-TLS 및 DNS-over-HTTPS 프로토콜을 지원하며, JSON을 내보낼 수 있음.
> 더 많은 정보: <https://github.com/ogham/dog#examples>.

- 호스트 이름과 연결된 IP를 조회 (A 레코드):

`dog {{example.com}}`

- 특정 도메인 이름과 관련된 MX 레코드 유형을 쿼리:

`dog {{example.com}} MX`

- 쿼리할 특정 DNS 서버를 지정 (예. Cloudflare):

`dog {{example.com}} MX @{{1.1.1.1}}`

- UDP가 아닌 TCP를 통한 쿼리:

`dog {{example.com}} MX @{{1.1.1.1}} {{[-T|--tcp]}}`

- 명시적 인수를 사용하여 TCP를 통해 특정 도메인 이름과 연결된 MX 레코드 유형을 쿼리:

`dog {{[-q|--query]}} {{example.com}} {{[-t|--type]}} MX {{[-n|--nameserver]}} {{1.1.1.1}} {{[-T|--tcp]}}`

- DoH(DNS over HTTPS)를 사용하여 호스트 이름(A 레코드)과 연결된 IP를 조회:

`dog {{example.com}} {{[-H|--https]}} @{{https://cloudflare-dns.com/dns-query}}`
