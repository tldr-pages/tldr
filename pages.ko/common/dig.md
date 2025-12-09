# dig

> DNS 조회 유틸리티.
> 더 많은 정보: <https://manned.org/dig>.

- 호스트이름과 관련된 IP 조회하기 (A records):

`dig +short {{example.com}}`

- 주어진 도메인 이름과 관련된 메일 서버 조회하기 (MX record):

`dig +short {{example.com}} MX`

- 쿼리할 대체 DNS 서버를 지정하기:

`dig @{{8.8.8.8}} {{example.com}}`

- IP 주소에서 역방향 DNS 조회하기 (PTR record):

`dig -x {{8.8.8.8}}`

- 영역에 대해 권한있는 이름 서버들을 찾고 SOA 레코드들 표시하기:

`dig +nssearch {{example.com}}`

- 반복적인 쿼리들을 수행하고 도메인 이름을 분석하기 위해 전체 추적 경로를 표시하기:

`dig +trace {{example.com}}`
