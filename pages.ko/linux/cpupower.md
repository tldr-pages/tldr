# cpupower

> CPU 전력 및 조정 옵션 관련 도구.
> 더 많은 정보: <https://manned.org/cpupower>.

- CPU 목록 나열:

`sudo cpupower --cpu {{all}} info`

- 모든 코어에 대한 정보 출력:

`sudo cpupower --cpu {{all}} info`

- 모든 CPU를 절전 주파수 관리자로 설정:

`sudo cpupower --cpu {{all}} frequency-set --governor {{powersave}}`

- CPU 0의 사용 가능한 주파수 [g]overnor 출력:

`sudo cpupower --cpu {{0}} frequency-info g | grep "analyzing\|governors"`

- CPU 4의 하드웨어 주파수를 사람이 읽기 쉬운 형식으로 출력:

`sudo cpupower --cpu {{4}} frequency-info --hwfreq --human`
