# spfquery

> 전송자 정책 프레임워크(SPF) 레코드를 조회하여 이메일 발신자를 검증합니다.
> 더 많은 정보: <https://manned.org/spfquery>.

- 특정 IP 주소가 지정된 이메일 주소에서 이메일을 보낼 수 있는지 확인:

`spfquery -ip {{8.8.8.8}} -sender {{보낸이@example.com}}`

- 디버깅 출력을 활성화:

`spfquery -ip {{8.8.8.8}} -sender {{보낸이@example.com}} --debug`
