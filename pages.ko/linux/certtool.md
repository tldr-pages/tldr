# certtool

> PKI structures using GnuTLS를 사용하여 X.509 인증서, 키 및 PKI 구조 생성 및 관리.
> 더 많은 정보: <https://gnutls.org/manual/gnutls.html#certtool-Invocation>.

- 개인 키 생성 후 파일로 저장:

`certtool {{[-p|--generate-privkey]}} --outfile {{경로/대상/개인키.key}}`

- 개인 키와 템플릿 파일을 사용하여 자체 서명 인증서 생성:

`certtool {{[-s|--generate-self-signed]}} --load-privkey {{경로/대상/개인키.key}} --template {{경로/대상/info.template}} --outfile {{경로/대상/인증서.crt}}`

- 인증서 서명 요청 (CSR) 생성:

`certtool {{[-q|--generate-request]}} --load-privkey {{경로/대상/개인키.key}} --template {{경로/대상/info.template}} --outfile {{경로/대상/request.csr}}`

- 인증 기관 (CA) 인증서 생성:

`certtool {{[-s|--generate-self-signed]}} --load-privkey {{경로/대상/ca.key}} --template {{경로/대상/ca.template}} --outfile {{경로/대상/ca.crt}}`

- CA 인증서를 기준으로 인증서 검증:

`certtool --verify --infile {{경로/대상/인증서.crt}} --load-ca-certificate {{경로/대상/ca.crt}}`
