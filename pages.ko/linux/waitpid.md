# waitpid

> 임의의 프로세스 종료를 대기.
> 같이 보기: `wait`.
> 더 많은 정보: <https://manned.org/waitpid.1>.

- 지정된 PID의 모든 프로세스가 종료될 때까지 대기:

`waitpid {{pid1 pid2 ...}}`

- 최대 `n`초 동안 대기:

`waitpid --timeout {{n}} {{pid1 pid2 ...}}`

- 지정된 PID가 이미 종료된 경우에도 오류 발생하지 않음:

`waitpid --exited {{pid1 pid2 ...}}`

- 지정된 프로세스 중 `n`개가 종료될 때까지 대기:

`waitpid --count {{n}} {{pid1 pid2 ...}}`

- 도움말 표시:

`waitpid -h`
