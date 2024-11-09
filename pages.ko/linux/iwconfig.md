# iwconfig

> 무선 네트워크 인터페이스의 매개변수를 구성하고 표시합니다.
> 더 많은 정보: <https://manned.org/iwconfig>.

- 모든 인터페이스의 매개변수 및 통계 표시:

`iwconfig`

- 특정 인터페이스의 매개변수 및 통계 표시:

`iwconfig {{인터페이스}}`

- 특정 인터페이스의 ESSID(네트워크 이름) 설정 (예: eth0 또는 wlp2s0):

`iwconfig {{인터페이스}} {{새_네트워크_이름}}`

- 특정 인터페이스의 운영 모드 설정:

`iwconfig {{인터페이스}} mode {{Ad-Hoc|Managed|Master|Repeater|Secondary|Monitor|Auto}}`
