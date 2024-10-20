# shutdown

> 컴퓨터를 종료, 재시작 또는 로그오프하는 도구입니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- 현재 컴퓨터 종료:

`shutdown /s`

- 현재 컴퓨터 강제 종료:

`shutdown /s /f`

- 현재 컴퓨터 즉시 재시작:

`shutdown /r /t 0`

- 현재 컴퓨터 최대 절전 모드:

`shutdown /h`

- 현재 컴퓨터 로그오프:

`shutdown /l`

- 종료 전 대기 시간 지정:

`shutdown /s /t {{8}}`

- 대기 시간이 만료되지 않은 종료 시퀀스 중단:

`shutdown /a`

- 원격 컴퓨터 종료:

`shutdown /m {{\\호스트명}}`
