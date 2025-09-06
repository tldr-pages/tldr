# openssl s_client

> TLS 클라이언트 연결을 생성하는 OpenSSL 명령어.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

- 도메인 인증서의 시작 및 만료 날짜 표시:

`openssl s_client -connect {{호스트}}:{{포트}} 2>/dev/null | openssl x509 -noout -dates`

- SSL/TLS 서버에서 제공하는 인증서 표시:

`openssl s_client -connect {{호스트}}:{{포트}} </dev/null`

- SSL/TLS 서버에 연결할 때 서버 이름 지시자(SNI) 설정:

`openssl s_client -connect {{호스트}}:{{포트}} -servername {{호스트명}}`

- HTTPS 서버의 전체 인증서 체인 표시:

`openssl s_client -connect {{호스트}}:443 -showcerts </dev/null`
