# ipcrm

> IPC(프로세스 간 통신) 리소스를 삭제합니다.
> 더 많은 정보: <https://manned.org/ipcrm>.

- ID로 공유 메모리 세그먼트 삭제:

`ipcrm --shmem-id {{공유_메모리_ID}}`

- 키로 공유 메모리 세그먼트 삭제:

`ipcrm --shmem-key {{공유_메모리_키}}`

- ID로 IPC 큐 삭제:

`ipcrm --queue-id {{IPC_큐_ID}}`

- 키로 IPC 큐 삭제:

`ipcrm --queue-key {{IPC_큐_키}}`

- ID로 세마포어 삭제:

`ipcrm --semaphore-id {{세마포어_ID}}`

- 키로 세마포어 삭제:

`ipcrm --semaphore-key {{세마포어_키}}`

- 모든 IPC 리소스 삭제:

`ipcrm --all`
