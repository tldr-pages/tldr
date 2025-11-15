# ipcs

> System V IPC 설비의 사용 정보 보기: 공유 메모리 세그먼트, 메시지 큐, 세마포어 배열.
> 같이 보기: 좀 더 유연한 도구인 `lsipc`, IPC 설비 생성을 위한 `ipcmk`, 삭제를 위한 `ipcrm`.
> 더 많은 정보: <https://manned.org/ipcs>.

- 모든 활성 IPC 설비에 대한 정보 보기:

`ipcs`

- 활성 공유 [m]메모리 세그먼트, 메시지 [q]큐 또는 [s]세마포어 집합에 대한 정보 보기:

`ipcs {{--shmems|--queues|--semaphores}}`

- 특정 [i]D를 가진 자원에 대한 전체 세부 사항 보기:

`ipcs {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{자원_ID}}`

- [l]리미트를 [b]바이트 또는 사람이 읽기 쉬운 형식으로 보기:

`ipcs {{[-l|--limits]}} {{--bytes|--human}}`

- 현재 사용에 대한 [u]요약 보기:

`ipcs {{[-u|--summary]}}`

- 모든 IPC 설비에 대한 [c]만든이 및 소유자의 UID와 PID 보기:

`ipcs {{[-c|--creator]}}`

- 모든 IPC 설비에 대한 마지막 작업자의 [p]ID 보기:

`ipcs {{[-p|--pid]}}`

- 모든 IPC 설비에 대한 마지막 접근 [t]시각 보기:

`ipcs {{[-t|--time]}}`
