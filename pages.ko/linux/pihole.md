# pihole

> Pi-hole 광고 차단 DNS 서버의 터미널 인터페이스.
> 더 많은 정보: <https://docs.pi-hole.net/main/pihole-command>.

- Pi-hole 데몬의 상태 확인:

`pihole status`

- Pi-hole 및 Gravity 업데이트:

`pihole {{[-up|updatePihole]}}`

- 데몬 시작 또는 중지:

`pihole {{enable|disable}}`

- 도메인 화이트리스트 또는 블랙리스트에 추가:

`pihole {{allowlist|denylist}} {{example.com}}`

- 도메인을 목록에서 검색:

`pihole {{[-q|query]}} {{example.com}}`

- 연결의 실시간 로그 열기:

`pihole {{[-t|tail]}}`
