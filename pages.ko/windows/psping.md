# psping

> TCP ping, 대기 시간 및 대역폭 측정을 포함하는 ping 도구입니다.
> 더 많은 정보: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- ICMP를 사용하여 호스트 확인:

`psping {{호스트명}}`

- TCP 포트를 통해 호스트 확인:

`psping {{호스트명}}:{{포트}}`

- 횟수 지정 및 출력 없이 수행:

`psping {{호스트명}} -n {{pings}} -q`

- TCP를 통해 대상에 50번 ping을 보내고 결과를 히스토그램으로 생성:

`psping {{호스트명}}:{{포트}} -q -n {{50}} -h`

- 도움말 표시:

`psping /?`
