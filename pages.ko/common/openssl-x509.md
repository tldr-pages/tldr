# openssl x509

> X.509 인증서를 관리하기 위한 OpenSSL 명령어.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- 인증서 정보 표시:

`openssl x509 -in {{파일이름.crt}} -noout -text`

- 인증서 만료 날짜 표시:

`openssl x509 -enddate -noout -in {{파일이름.pem}}`

- 인증서를 이진 DER 인코딩과 텍스트 PEM 인코딩 간 변환:

`openssl x509 -inform {{der}} -outform {{pem}} -in {{원본_인증서_파일}} -out {{변환된_인증서_파일}}`

- 인증서의 공개 키를 파일에 저장:

`openssl x509 -in {{인증서_파일}} -noout -pubkey -out {{출력_파일}}`
