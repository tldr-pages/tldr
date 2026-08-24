# openssl speed

> OpenSSL 알고리즘의 성능을 벤치마크하는 명령어.
> 더 많은 정보: <https://docs.openssl.org/master/man1/openssl-speed/>.

- 사용 가능한 모든 알고리즘 벤치마크:

`openssl speed`

- 주요 알고리즘 벤치마크:

`openssl speed {{md5 sha1 sha256 aes rsa}}`

- 특정 EVP 암호 알고리즘 벤치마크:

`openssl speed -evp {{aes-256-cbc}}`

- 지정한 시간(초) 동안 벤치마크:

`openssl speed -seconds {{10}}`

- CPU 시간 대신 실제 경과시간으로 측정:

`openssl speed -elapsed`

- 기계 처리용 출력 형식으로 결과 표시:

`openssl speed -mr`

- 모든 CPU 코어를 사용해 병렬 벤치마크:

`openssl speed -multi $(nproc)`
