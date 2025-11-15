# sntpd

> SNTP 서버.
> 수동으로 실행해서는 안 됩니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/sntpd.8.html>.

- 데몬 시작:

`sntpd`

- 기존 상태를 로컬 시계로 덮어쓰고 (계층 1), 다른 (더 높은 계층) 서버와 동기화하지 않고 마스터/주 서버를 실행:

`sntpd -L`

- 사용자 지정 파일을 SNTP 상태로 사용:

`sntpd -z {{경로/대상/state.bin}}`
