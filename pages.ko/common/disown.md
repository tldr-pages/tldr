# disown

> 하위 프로세스가 연결된 쉘 외부에서 작동하도록 허용.
> `jobs` 명령도 참조.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- 현재 작업을 해제:

`disown`

- 특정 작업을 해제:

`disown %{{작업_번호}}`

- 모든 작업 해제:

`disown -a`

- 작업을 유지 (해제하지 않음), 쉘 종료 시 향후 SIGHUP이 수신되지 않도록 표시:

`disown -h %{{작업_번호}}`
