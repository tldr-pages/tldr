# openssl ts

> OpenSSL 명령어로 타임스탬프를 생성하고 검증합니다.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>.

- 특정 파일의 SHA-512 타임스탬프 요청을 생성하고 `file.tsq`에 출력:

`openssl ts -query -data {{경로/대상/파일}} -sha512 -out {{경로/대상/파일.tsq}}`

- 특정 타임스탬프 응답 파일의 날짜 및 메타데이터 확인:

`openssl ts -reply -in {{경로/대상/파일.tsr}} -text`

- SSL 인증서 파일을 사용하여 서버로부터 타임스탬프 요청 파일과 타임스탬프 응답 파일 검증:

`openssl ts -verify -in {{경로/대상/파일.tsr}} -queryfile {{경로/대상/파일.tsq}} -partial_chain -CAfile {{경로/대상/cert.pem}}`

- 키 및 서명 인증서를 사용하여 요청에 대한 타임스탬프 응답을 생성하고 `file.tsr`에 출력:

`openssl ts -reply -queryfile {{경로/대상/파일.tsq}} -inkey {{경로/대상/tsakey.pem}} -signer tsacert.pem -out {{경로/대상/파일.tsr}}`
