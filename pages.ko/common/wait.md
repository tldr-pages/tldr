# wait

> 프로세스가 완료될 때까지 대기.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-wait>.

- 프로세스 ID (PID)를 사용하여 특정 프로세스가 종료될 때까지 대기하고 종료 상태 반환:

`wait {{pid}}`

- 호출한 셸에서 알고 있는 모든 프로세스가 종료될 때까지 대기:

`wait`

- 작업이 완료될 때까지 대기:

`wait %{{N}}`
