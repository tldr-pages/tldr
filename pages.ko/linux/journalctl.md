# journalctl

> systemd 저널을 조회합니다.
> 더 많은 정보: <https://manned.org/journalctl>.

- 현재 [b]부트에서 우선순위 레벨 3(오류)로 모든 메시지 표시:

`journalctl -b --priority=3`

- 2일 이상된 저널 로그 삭제:

`journalctl --vacuum-time=2d`

- 마지막 N줄만 표시하고 새 메시지를 [f]팔로우(전통적인 syslog의 `tail -f`처럼) 표시:

`journalctl --lines {{N}} --follow`

- 특정 [u]유닛의 모든 메시지 표시:

`journalctl --unit {{유닛}}`

- 마지막으로 시작된 이후 유닛의 로그 표시:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{유닛}})`

- 시간 범위 내의 메시지 필터링(타임스탬프 또는 "yesterday" 같은 플레이스홀더 사용 가능):

`journalctl --since {{now|today|yesterday|tomorrow}} --until "{{YYYY-MM-DD HH:MM:SS}}"`

- 특정 프로세스의 모든 메시지 표시:

`journalctl _PID={{pid}}`

- 특정 실행 파일의 모든 메시지 표시:

`journalctl {{경로/대상/실행_파일}}`
