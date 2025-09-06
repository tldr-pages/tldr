# host

> 도메인 네임 서버 조회.
> 더 많은 정보: <https://manned.org/host>.

- 도메인의 A, AAAA 및 MX 레코드 조회:

`host {{도메인}}`

- 도메인의 필드 (CNAME, TXT, ...) 조회:

`host -t {{필드}} {{도메인}}`

- IP 역방향 조회:

`host {{ip_주소}}`

- 쿼리할 대체 DNS 서버를 지정:

`host {{도메인}} {{8.8.8.8}}`
