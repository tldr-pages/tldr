# sslscan

> 서버에서 지원하는 SSL/TLS 프로토콜 및 암호를 검사.
> 더 많은 정보: <https://github.com/rbsec/sslscan>.

- 포트 443에서 서버 테스트:

`sslscan {{example.com}}`

- 지정된 포트에서 테스트:

`sslscan {{example.com}}:{{465}}`

- 인증서 정보 표시:

`testssl --show-certificate {{example.com}}`
