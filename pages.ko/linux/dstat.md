# dstat

> 시스템 리소스 통계 생성을 위한 다재다능한 도구.
> 더 많은 정보: <https://github.com/dstat-real/dstat>.

- CPU, 디스크, 네트워크, 페이징 및 시스템 통계 표시:

`dstat`

- 5초마다 통계를 표시하고 4번만 업데이트:

`dstat {{5}} {{4}}`

- CPU 및 메모리 통계만 표시:

`dstat --cpu --mem`

- 사용 가능한 모든 dstat 플러그인 나열:

`dstat --list`

- 가장 많은 메모리와 CPU를 사용하는 프로세스 표시:

`dstat --top-mem --top-cpu`

- 배터리 백분율 및 남은 배터리 시간 표시:

`dstat --battery --battery-remain`
