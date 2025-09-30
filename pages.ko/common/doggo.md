# doggo

> 사람을 위한 DNS 클라이언트.
> Golang으로 작성됨.
> 더 많은 정보: <https://github.com/mr-karan/doggo/blob/main/docs/src/content/docs/guide/reference.md>.

- 간단한 DNS 조회를 수행:

`doggo {{example.com}}`

- 특정 네임서버를 사용하여 MX 레코드를 쿼리:

`doggo MX {{codeberg.org}} @{{1.1.1.2}}`

- HTTPS를 통해 DNS 사용:

`doggo {{example.com}} @{{https://dns.quad9.net/dns-query}}`

- JSON 형식으로 출력:

`doggo {{example.com}} {{[-J|--json]}} | jq '{{.responses[0].answers[].address}}'`

- 역방향 DNS 조회를 수행:

`doggo {{[-x|--reverse]}} {{8.8.4.4}} --short`
