# ahost

> 호스트 이름 또는 IP 주소와 연결된 A 또는 AAAA 레코드를 표시하는 DNS 조회 도구.
> 더 많은 정보: <https://manned.org/ahost>.

- 호스트 이름 또는 IP 주소와 연결된 `A` 또는 `AAAA` 레코드 출력:

`ahost {{example.com}}`

- 추가 디버깅 출력을 표시:

`ahost -d {{example.com}}`

- 지정된 유형의 레코드 표시:

`ahost -t {{a|aaaa|u}} {{example.com}}`
