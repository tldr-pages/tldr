# speedtest-cli

> <https://speedtest.net>를 사용하여 인터넷 대역폭 테스트.
> 공식 CLI는 `speedtest`를 참조하세요.
> 더 많은 정보: <https://github.com/sivel/speedtest-cli>.

- 속도 테스트 실행:

`speedtest-cli`

- 속도 테스트를 실행하고 비트 대신 바이트 단위로 값 표시:

`speedtest-cli --bytes`

- `HTTP` 대신 `HTTPS`를 사용하여 속도 테스트 실행:

`speedtest-cli --secure`

- 다운로드 테스트를 수행하지 않고 속도 테스트 실행:

`speedtest-cli --no-download`

- 속도 테스트를 실행하고 결과 이미지를 생성:

`speedtest-cli --share`

- 거리별로 정렬된 모든 `speedtest.net` 서버 나열:

`speedtest-cli --list`

- 특정 speedtest.net 서버로 속도 테스트 실행:

`speedtest-cli --server {{서버_ID}}`

- 속도 테스트를 실행하고 결과를 JSON 형식으로 표시 (진행 정보 억제):

`speedtest-cli --json`
