# sntp

> 매우 간단한 네트워크 시간 프로토콜 클라이언트 프로그램.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/sntp.1>.

- 지정된 SNTP 서버에 쿼리하고 시간을 표시:

`sntp {{pool.ntp.org}}`

- 지정된 SNTP 서버로 시스템 시계를 동기화:

`sudo sntp -S {{pool.ntp.org}}`

- 디버그 로깅 활성화:

`sntp -d {{pool.ntp.org}}`
