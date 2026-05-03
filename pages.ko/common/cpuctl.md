# cpuctl

> 커멘드라인에서 시스템 CPU를 제어하고 상태를 확인하는 도구.
> 참고: 시스템에는 최소 하나의 CPU가 항상 온라인 상태로 유지되어야 함.
> 더 많은 정보: <https://man.netbsd.org/cpuctl.8>.

- 시스템 내 각 CPU의 현재 상태와 마지막 상태 변경 시간 출력:

`sudo cpuctl list`

- 지정된 CPU들을 오프라인으로 설정:

`sudo cpuctl offline {{cpu_번호1 cpu_번호2 ...}}`

- 지정된 CPU들을 온라인으로 설정:

`sudo cpuctl online {{cpu_번호1 cpu_번호2 ...}}`
