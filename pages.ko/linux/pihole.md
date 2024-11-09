# pihole

> Pi-hole 광고 차단 DNS 서버의 터미널 인터페이스.
> 더 많은 정보: <https://docs.pi-hole.net/core/pihole-command/>.

- Pi-hole 데몬의 상태 확인:

`pihole status`

- Pi-hole 및 Gravity 업데이트:

`pihole -up`

- 시스템 상태 자세히 모니터링:

`pihole chronometer`

- 데몬 시작 또는 중지:

`pihole {{enable|disable}}`

- 데몬 재시작 (서버 자체는 아님):

`pihole restartdns`

- 도메인 화이트리스트 또는 블랙리스트에 추가:

`pihole {{whitelist|blacklist}} {{example.com}}`

- 도메인을 목록에서 검색:

`pihole query {{example.com}}`

- 연결의 실시간 로그 열기:

`pihole tail`
