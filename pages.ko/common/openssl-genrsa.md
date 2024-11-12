# openssl genrsa

> RSA 개인 키를 생성하는 OpenSSL 명령어.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>.

- 2048비트 RSA 개인 키를 `stdout`에 생성:

`openssl genrsa`

- 임의 비트 수의 RSA 개인 키를 출력 파일에 저장:

`openssl genrsa -out {{출력_파일.key}} {{1234}}`

- RSA 개인 키를 생성하고 AES256으로 암호화 (암호를 입력하라는 메시지가 표시됨):

`openssl genrsa {{-aes256}}`
