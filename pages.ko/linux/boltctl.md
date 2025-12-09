# boltctl

> 썬더볼트 장치를 제어합니다.
> 더 많은 정보: <https://manned.org/boltctl>.

- 연결된 (및 승인된) 장치 나열:

`boltctl`

- 승인되지 않은 장치를 포함하여 연결된 장치 나열:

`boltctl list`

- 장치를 일시적으로 승인:

`boltctl authorize {{장치_UUID}}`

- 장치를 승인하고 기억:

`boltctl enroll {{장치_UUID}}`

- 이전에 승인된 장치 승인 취소:

`boltctl forget {{장치_UUID}}`

- 장치에 대한 추가 정보 표시:

`boltctl info {{장치_UUID}}`
