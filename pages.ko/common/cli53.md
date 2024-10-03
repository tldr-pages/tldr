# cli53

> Amazon Route 53용 명령줄 도구.
> 더 많은 정보: <https://github.com/barnybug/cli53>.

- 도메인 나열:

`cli53 list`

- 도메인 생성:

`cli53 create {{도메인주소.com}} --comment "{{코멘트}}"`

- 바인드 존 파일을 `stdout`으로 내보내기:

`cli53 export {{도메인주소.com}}`

- 동일한 영역의 상대 레코드를 가리키는 `www` 하위 도메인을 생성:

`cli53 {{rc|rrcreate}} {{도메인주소.com}} {{'www 300 CNAME lb'}}`

- 외부 주소를 가리키는 `www` 하위 도메인을 생성 (점으로 끝나야 함):

`cli53 {{rc|rrcreate}} {{도메인주소.com}} {{'www 300 CNAME lb.externalhost.com.'}}`

- IP 주소를 가리키는 `www` 하위 도메인을 생성:

`cli53 {{rc|rrcreate}} {{도메인주소.com}} {{'www 300 A 150.130.110.1'}}`

- 다른 IP를 가리키는 `www` 하위 도메인을 교체:

`cli53 {{rc|rrcreate}} --replace {{'www 300 A 150.130.110.2'}}`

- A 레코드 삭제:

`cli53 {{rd|rrdelete}} {{도메인주소.com}} {{www}} {{A}}`
