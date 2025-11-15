# testssl

> 서버에서 지원하는 SSL/TLS 프로토콜 및 암호를 확인.
> 더 많은 정보: <https://testssl.sh/doc/testssl.1.html>.

- 서버 테스트 (모든 검사를 실행) 포트 443에서:

`testssl {{example.com}}`

- 다른 포트 테스트:

`testssl {{example.com:465}}`

- 사용 가능한 프로토콜만 확인:

`testssl --protocols {{example.com}}`

- 취약점만 확인:

`testssl --vulnerable {{example.com}}`

- HTTP 보안 헤더만 확인:

`testssl --headers {{example.com}}`

- 다른 STARTTLS 지원 프로토콜 테스트:

`testssl --starttls {{ftp|smtp|pop3|imap|xmpp|sieve|xmpp-server|telnet|ldap|irc|lmtp|nntp|postgres|mysql}} {{example.com}}:{{포트}}`
