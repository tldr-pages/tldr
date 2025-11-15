# ntpctl

> 실행 중인 OpenNTPD 인스턴스에 대한 정보를 표시.
> 더 많은 정보: <https://man.openbsd.org/ntpctl>.

- 모든 데이터 표시:

`ntpctl -s {{[a|all]}}`

- 각 피어에 대한 정보 표시:

`ntpctl -s {{[p|peers]}}`

- 피어와 센서의 상태 및 시스템 시계 동기화 여부 표시:

`ntpctl -s {{[s|status]}}`

- 각 센서에 대한 정보 표시:

`ntpctl -s {{[S|Sensors]}}`
