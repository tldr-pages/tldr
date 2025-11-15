# cbatticon

> 시스템 트레이에 위치하는 가볍고 빠른 배터리 아이콘.
> 더 많은 정보: <https://github.com/valr/cbatticon>.

- 시스템 트레이에 배터리 아이콘 표시:

`cbatticon`

- 배터리 아이콘을 표시하고 업데이트 간격을 20초로 설정:

`cbatticon --update-interval {{20}}`

- 사용 가능한 아이콘 유형 나열:

`cbatticon --list-icon-types`

- 특정 아이콘 유형으로 배터리 아이콘 표시:

`cbatticon --icon-type {{standard|notification|symbolic}}`

- 사용 가능한 전원 공급 장치 나열:

`cbatticon --list-power-supplies`

- 특정 배터리에 대한 배터리 아이콘 표시:

`cbatticon {{BAT0}}`

- 배터리 수준이 설정된 임계 수준에 도달했을 때 실행할 명령과 함께 배터리 아이콘 표시:

`cbatticon --critical-level {{5}} --command-critical-level {{poweroff}}`
