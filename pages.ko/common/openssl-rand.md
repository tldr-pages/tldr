# openssl rand

> 암호학적으로 안전한 PRNG를 사용하여 랜덤 바이트를 생성하는 명령어.
> 더 많은 정보: <https://docs.openssl.org/master/man1/openssl-rand/>.

- 8바이트(16문자) hex 문자열 생성 후 `stdout` 출력:

`openssl rand -hex 8`

- 20바이트를 랜덤으로 생성 후 base64로 인코딩하여 생성:

`openssl rand -base64 20`

- 랜덤 바이트를 파일로 저장 (인코딩 없음):

`openssl rand -out {{경로/대상/파일}} {{길이}}`

- 1 KiB/MiB/GiB/TiB 크기의 랜덤 바이트를 hex 또는 base64로 생성:

`openssl rand -{{hex|base64}} 1{{K|M|G|T}}`
