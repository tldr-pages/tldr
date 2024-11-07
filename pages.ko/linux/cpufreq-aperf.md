# cpufreq-aperf

> 일정 시간 동안 평균 CPU 주파수를 계산합니다.
> 루트 권한이 필요합니다.
> 더 많은 정보: <https://manned.org/cpufreq-aperf>.

- 모든 CPU 코어와 1초 새로고침 간격으로 계산 시작:

`sudo cpufreq-aperf`

- CPU 1만 계산 시작:

`sudo cpufreq-aperf -c {{1}}`

- 모든 CPU 코어에 대해 3초 새로고침 간격으로 계산 시작:

`sudo cpufreq-aperf -i {{3}}`

- 한 번만 계산:

`sudo cpufreq-aperf -o`
