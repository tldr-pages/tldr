# openssl prime

> 소수를 계산하기 위한 OpenSSL 명령어.
> 더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>.

- 2048비트 소수를 생성하고 16진수로 표시:

`openssl prime -generate -bits 2048 -hex`

- 주어진 숫자가 소수인지 확인:

`openssl prime {{숫자}}`
