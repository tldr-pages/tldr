# openssl dgst

> OpenSSL 명령어로, 메시지 다이제스트 값을 생성하고 서명 작업을 수행합니다.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

- 파일의 SHA256 다이제스트 값을 계산하여 특정 파일에 저장:

`openssl dgst -sha256 -binary -out {{출력_파일}} {{입력_파일}}`

- RSA 키를 사용하여 파일에 서명하고 결과를 특정 파일에 저장:

`openssl dgst -sign {{개인_키_파일}} -sha256 -sigopt rsa_padding_mode:pss -out {{출력_파일}} {{입력_파일}}`

- RSA 서명 검증:

`openssl dgst -verify {{공개_키_파일}} -signature {{서명_파일}} -sigopt rsa_padding_mode:pss {{서명_메시지_파일}}`

- ECDSA 키를 사용하여 파일에 서명:

`openssl dgst -sign {{개인_키_파일}} -sha256 -out {{출력_파일}} {{입력_파일}}`

- ECDSA 서명 검증:

`openssl dgst -verify {{공개_키_파일}} -signature {{서명_파일}} {{서명_메시지_파일}}`
