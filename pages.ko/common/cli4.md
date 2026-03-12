# cli4

> Cloudflare API를 위한 Python 명령줄 인터페이스.
> 더 많은 정보: <https://github.com/cloudflare/python-cloudflare>.

- 계정 정보를 표시:

`cli4 {{/사용자}}`

- 모든 zone 목록을 표시:

`cli4 {{/zones}}`

- 특정 zone의 DNS 레코드를 표시:

`cli4 {{/zones/:example.com/dns_레코드}}`

- 새로운 DNS 레코드를 생성:

`cli4 --post {{name=example.com}} {{type=A}} {{content=192.0.2.1}} {{/zones/:example.com/dns_레코드}}`

- 기존 DNS 레코드를 업데이트:

`cli4 --put {{name=sub.example.com}} {{type=A}} {{content=192.0.2.2}} {{/zones/:example.com/dns_레코드/:레코드_아이디}}`

- DNS 레코드를 삭제:

`cli4 --delete {{/zones/:example.com/dns_레코드/:레코드_아이디}}}`

- 특정 zone의 캐시를 모두 삭제:

`cli4 --post {{purge_everything=true}} {{/zones/:example.com/purge_cache}}`
