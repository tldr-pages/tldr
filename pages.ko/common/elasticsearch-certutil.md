# elasticsearch-certutil

> Elasticsearch 보안을 위한 SSL 인증서를 생성하고 관리하는 도구.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/certutil>.

- 기본 옵션으로 새로운 Certificate Authority (CA) 생성:

`elasticsearch-certutil ca`

- 내장 CA를 사용하여 새로운 인증서 생성:

`elasticsearch-certutil cert`

- 비대화식으로 PEM 형식 인증서 파일 생성:

`elasticsearch-certutil cert {{[-s|--silent]}} --pem`

- 내장 CA를 사용하여 HTTP 인증서 생성:

`elasticsearch-certutil http`

- 비대화식으로 transport 인증서 생성:

`elasticsearch-certutil transport {{[-s|--silent]}}`

- 인증서 서명 요청 (CSR) 생성:

`elasticsearch-certutil csr`

- keystore 암호 생성:

`elasticsearch-certutil password`

- 지정한 값으로 keystore 암호 생성:

`elasticsearch-certutil password --pass {{비밀번호}}`
