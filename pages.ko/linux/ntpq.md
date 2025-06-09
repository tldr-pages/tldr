# ntpq

> 네트워크 타임 프로토콜(NTP) 데몬 질의 도구.
> 더 많은 정보: <https://manned.org/man/ntpq.1>.

- 대화형 모드로 `ntpq` 시작:

`ntpq`

- NTP 피어 목록 출력:

`ntpq {{[-p|--peers]}}`

- IP 주소에서 호스트명을 해석하지 않고 NTP 피어 목록 출력:

`ntpq {{[-n|--numeric]}} {{[-p|--peers]}}`

- 디버깅 모드로 `ntpq` 사용:

`ntpq {{[-d|--debug-level]}}`

- NTP 시스템 변수 값 출력:

`ntpq {{[-c|--command]}} {{rv}}`
