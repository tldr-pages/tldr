# openssl genpkey

> 비대칭 키 쌍을 생성하는 OpenSSL 명령어.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html>.

- 2048비트 RSA 개인 키 생성 및 특정 파일에 저장:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{파일이름.key}}`

- 곡선 `prime256v1`을 사용하여 타원 곡선 개인 키 생성 및 특정 파일에 저장:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{파일이름.key}}`

- `ED25519` 타원 곡선 개인 키 생성 및 특정 파일에 저장:

`openssl genpkey -algorithm {{ED25519}} -out {{파일이름.key}}`
