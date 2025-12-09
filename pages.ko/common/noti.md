# noti

> 프로세스를 모니터링하고 배너 알림을 트리거.
> 더 많은 정보: <https://github.com/variadico/noti>.

- tar가 파일 압축을 완료하면 알림 표시:

`noti {{tar -cjf example.tar.bz2 example/}}`

- 감시할 명령어 뒤에 추가해도 알림 표시:

`{{감시할_명령어}}; noti`

- PID를 통해 프로세스를 모니터링하고 PID가 사라지면 알림 트리거:

`noti -w {{프로세스_ID}}`
