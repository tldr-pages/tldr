# swaks

> 스위스 아미 나이프 SMTP, 다목적 SMTP 트랜잭션 테스터.
> 더 많은 정보: <https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- `test-server.example.net`의 포트 25에 `user@example.com`으로 표준 테스트 이메일 전송:

`swaks --to {{user@example.com}} --server {{test-server.example.net}}`

- 사용자 `me@example.com`으로 CRAM-MD5 인증을 요구하며 표준 테스트 이메일 전송. 이메일 본문에 "X-Test" 헤더 추가:

`swaks --to {{user@example.com}} --from {{me@example.com}} --auth {{CRAM-MD5}} --auth-user {{me@example.com}} --header-X-Test "{{test_email}}"`

- 첨부 파일로 EICAR을 사용하여 바이러스 스캐너 테스트. 메시지 DATA 부분은 표시하지 않음:

`swaks -t {{user@example.com}} --attach - --server {{test-server.example.com}} --suppress-data {{경로/대상/eicar.txt}}`

- 이메일 본문에 GTUBE를 사용하여 스팸 스캐너 테스트, `example.com`의 MX 레코드를 통해 라우팅:

`swaks --to {{user@example.com}} --body {{경로/대상/gtube_파일}}`

- UNIX 도메인 소켓 파일을 통해 LMTP 프로토콜을 사용하여 `user@example.com`으로 표준 테스트 이메일 전송:

`swaks --to {{user@example.com}} --socket {{/var/lda.sock}} --protocol {{LMTP}}`
