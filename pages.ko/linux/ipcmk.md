# ipcmk

> IPC(프로세스 간 통신) 리소스 생성.
> 더 많은 정보: <https://manned.org/ipcmk>.

- 공유 메모리 세그먼트 생성:

`ipcmk --shmem {{세그먼트_크기_바이트}}`

- 세마포어 생성:

`ipcmk --semaphore {{요소_크기}}`

- 메시지 큐 생성:

`ipcmk --queue`

- 특정 권한으로 공유 메모리 세그먼트 생성 (기본값은 0644):

`ipcmk --shmem {{세그먼트_크기_바이트}} {{8진수_권한}}`
