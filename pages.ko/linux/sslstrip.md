# sslstrip

> Moxie Marlinspike의 Secure Sockets Layer (SSL) 스트리핑 공격을 수행합니다.
> ARP 스푸핑 공격을 함께 수행합니다.
> 더 많은 정보: <https://www.kali.org/tools/sslstrip/>.

- 기본으로 포트 10000에서 HTTPS POST 트래픽만 로깅:

`sslstrip`

- 포트 8080에서 HTTPS POST 트래픽만 로깅:

`sslstrip --listen={{8080}}`

- 포트 8080에서 서버와 주고받는 모든 SSL 트래픽 로깅:

`sslstrip --ssl --listen={{8080}}`

- 포트 8080에서 서버와 주고받는 모든 SSL 및 HTTP 트래픽 로깅:

`sslstrip --listen={{8080}} --all`

- 로그를 저장할 파일 경로 지정:

`sslstrip --listen={{8080}} --write={{경로/대상/파일}}`

- 도움말 표시:

`sslstrip --help`
