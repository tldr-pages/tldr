# trace-cmd

> Ftrace Linux 커널 내부 트레이서와 상호 작용하는 도구.
> 이 도구는 root 사용자로만 실행됩니다.
> 더 많은 정보: <https://manned.org/trace-cmd>.

- 트레이싱 시스템의 상태 표시:

`trace-cmd stat`

- 사용 가능한 트레이서 나열:

`trace-cmd list -t`

- 특정 플러그인으로 트레이싱 시작:

`trace-cmd start -p {{timerlat|osnoise|hwlat|blk|mmiotrace|function_graph|wakeup_dl|wakeup_rt|wakeup|function|nop}}`

- 트레이스 출력 보기:

`trace-cmd show`

- 트레이싱을 중지하지만 버퍼 유지:

`trace-cmd stop`

- 트레이스 버퍼 지우기:

`trace-cmd clear`

- 트레이스 버퍼 지우기 및 트레이싱 중지:

`trace-cmd reset`
