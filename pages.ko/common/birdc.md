# birdc

> BIRD 원격 제어.
> bird로부터 경로와 같은 정보를 검색하고 런타임 중에 구성을 수행.
> 더 많은 정보: <https://bird.network.cz/?get_doc&v=30&f=bird-4.html>.

- 원격 제어 콘솔을 열기:

`birdc`

- BIRD를 다시 시작하지 않고 구성을 다시 로드:

`birdc configure`

- BIRD의 현재 상태를 표시:

`birdc show status`

- 구성된 모든 프로토콜 표시:

`birdc show protocols`

- 프로토콜에 대한 모든 세부정보 표시:

`birdc show protocols {{upstream1}} all`

- 특정 AS 번호를 포함하는 모든 경로 표시:

`birdc "show route where bgp_path ~ [{{4242120045}}]"`

- 모든 최적 경로 표시:

`birdc show route primary`

- 특정 접두사에서 모든 경로의 모든 세부 정보를 표시:

`birdc show route for {{fd00:/8}} all`
