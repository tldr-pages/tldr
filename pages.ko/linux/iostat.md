# iostat

> 장치 및 파티션에 대한 통계 보고.
> 더 많은 정보: <https://manned.org/iostat>.

- 시스템 시작 이후의 CPU 및 디스크 통계 보고서 표시:

`iostat`

- 단위를 메가바이트로 변환한 CPU 및 디스크 통계 보고서 표시:

`iostat -m`

- CPU 통계 표시:

`iostat {{[-c|--compact]}}`

- 디스크 이름(및 LVM 포함)을 사용한 디스크 통계 표시:

`iostat -N`

- 장치 "sda"에 대한 디스크 이름을 포함한 확장 디스크 통계 표시:

`iostat -xN {{sda}}`

- 2초마다 CPU 및 디스크 통계의 증분 보고서 표시:

`iostat {{2}}`
