# systemd-cgtop

> 로컬 Linux 제어 그룹 계층의 최상위 제어 그룹을 CPU, 메모리, 디스크 I/O 부하에 따라 정렬하여 표시.
> 같이 보기: `top`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cgtop.html>.

- 대화형 보기 시작:

`systemd-cgtop`

- 정렬 순서 변경:

`systemd-cgtop --order={{cpu|memory|path|tasks|io}}`

- CPU 사용량을 백분율 대신 시간으로 표시:

`systemd-cgtop --cpu=percentage`

- 업데이트 간격을 초(또는 이러한 시간 단위 중 하나: `ms`, `us`, `min`)로 변경:

`systemd-cgtop --delay={{간격}}`

- 사용자 공간 프로세스만 계산 (커널 스레드는 제외):

`systemd-cgtop -P`
