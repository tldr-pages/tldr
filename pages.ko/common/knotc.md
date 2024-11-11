# knotc

> Knot DNS 서버 제어.
> 더 많은 정보: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- zone 편집 시작:

`knotc zone-begin {{zone}}`

- TTL이 3600인 A 레코드 설정:

`knotc zone-set {{zone}} {{서브도메인}} 3600 A {{IP_주소}}`

- zone 편집 완료:

`knotc zone-commit {{zone}}`

- 현재 zone 데이터 얻기:

`knotc zone-read {{zone}}`

- 현재 서버 구성 가져오기:

`knotc conf-read server`
