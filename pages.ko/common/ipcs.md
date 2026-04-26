# ipcs

> XSI IPC 자원(공유 메모리 세그먼트, 메시지 큐, 세마포어 등) 사용 정보에 대한 정보 표시.
> 더 많은 정보: <https://manned.org/ipcs.1p>.

- 모든([a]ll) IPC 정보 출력:

`ipcs -a`

- 활성 공유 메모리([m]emory), 메시지 큐([q]ueues) 또는 세마포어([s]empahore) 정보 출력:

`ipcs {{-m|-q|-s}}`

- 최대 허용 크기([b]ytes) 정보 출력:

`ipcs -b`

- 모든 IPC 자원의 생성자([c]reator's) 사용자 및 그룹 정보 출력:

`ipcs -c`

- 모든 IPC 자원에 대해 마지막 작업을 수행한 프로세스의 PID([p]ID) 표시:

`ipcs -p`

- 모든 IPC 자원 접근 시간([t]imes) 정보 출력:

`ipcs -t`

- 활성 메시지 큐, 공유 메모리의 현재([o]utstanding) 사용량 출력:

`ipcs -o`
