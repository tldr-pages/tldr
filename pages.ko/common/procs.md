# procs

> 활성 프로세스에 대한 정보를 표시.
> 더 많은 정보: <https://github.com/dalance/procs>.

- PID, 사용자, CPU 사용량, 메모리 사용량 및 시작한 명령을 보여주는 모든 프로세스 나열:

`procs`

- 트리 형태로 모든 프로세스 나열:

`procs --tree`

- 시작한 명령에 Zsh가 포함된 프로세스 정보 나열:

`procs {{zsh}}`

- CPU 시간으로 [a]scending 또는 [d]escending 순서로 정렬된 모든 프로세스 정보 나열:

`procs {{--sorta|--sortd}} cpu`

- PID, 명령 또는 사용자에 `41` 또는 `firefox`가 포함된 프로세스 정보 나열:

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- PID `41`과 명령 또는 사용자에 `zsh`가 포함된 프로세스 정보 나열:

`procs --and {{41}} {{zsh}}`
