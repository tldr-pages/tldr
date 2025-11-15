# turbostat

> 프로세서 토폴로지, 주파수, 온도, 전력 및 유휴 통계를 보고합니다.
> 더 많은 정보: <https://manned.org/turbostat.8>.

- 5초마다 통계 표시:

`sudo turbostat`

- 지정한 초마다 통계 표시:

`sudo turbostat -i {{초}}`

- 시스템 구성 헤더 정보를 해독하여 출력하지 않음:

`sudo turbostat --quiet`

- 헤더 정보 없이 1초마다 CPU에 대한 유용한 정보 표시:

`sudo turbostat --quiet --interval 1 --cpu 0-{{CPU_스레드_수}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- 도움말 표시:

`turbostat --help`
