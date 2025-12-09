# log

> 로그 시스템을 보기, 내보내기 및 구성.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/log.1.html>.

- 실시간 시스템 로그 스트리밍:

`log stream`

- 특정 PID를 가진 프로세스에서 `syslog`로 전송된 로그 스트리밍:

`log stream --process {{프로세스_ID}}`

- 특정 이름을 가진 프로세스에서 syslog로 전송된 로그 표시:

`log show --predicate "process == '{{프로세스_이름}}'"`

- 지난 한 시간 동안 모든 로그를 디스크에 내보내기:

`sudo log collect --last {{1h}} --output {{경로/대상/파일.logarchive}}`
