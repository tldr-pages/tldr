# dcgmi

> NVIDIA Data Center GPU를 관리하고 모니터링.
> 더 많은 정보: <https://developer.nvidia.com/dcgm>.

- 사용 가능한 모든 GPU와 이를 사용하는 프로세스 정보를 표시:

`dcgmi discovery {{[-l|--list]}}`

- 생성된 그룹 목록을 표시:

`dcgmi group {{[-l|--list]}}`

- 디바이스 0의 현재 사용 통계를 표시:

`dcgmi dmon {{[-e|--field-id]}}{{1001,1002,1003,1004,1005}}`

- 도움말 표시:

`dcgmi {{[-h|--help]}}`

- 하위 명령어의 도움말을 표시:

`dcgmi {{하위명령어}} {{[-h|--help]}}`
