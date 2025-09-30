# ethtool

> 네트워크 인터페이스 컨트롤러(NIC) 매개변수를 표시하고 수정합니다.
> 더 많은 정보: <https://manned.org/ethtool>.

- 인터페이스의 현재 설정 표시:

`ethtool {{eth0}}`

- 인터페이스의 드라이버 정보 표시:

`ethtool --driver {{eth0}}`

- 인터페이스에서 지원되는 모든 기능 표시:

`ethtool --show-features {{eth0}}`

- 인터페이스의 네트워크 사용 통계 표시:

`ethtool --statistics {{eth0}}`

- 인터페이스의 하나 이상의 LED를 10초 동안 깜박이기:

`ethtool --identify {{eth0}} {{10}}`

- 주어진 인터페이스의 링크 속도, 이중 모드 및 매개변수 자동 협상 설정:

`ethtool -s {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`
