# xinput

> 사용 가능한 입력 장치를 나열하고, 장치에 대한 정보를 쿼리하며, 입력 장치 설정을 변경.
> 더 많은 정보: <https://manned.org/xinput>.

- 모든 입력 장치 나열:

`xinput list`

- 입력 장치 비활성화:

`xinput disable {{id}}`

- 입력 장치 활성화:

`xinput enable {{id}}`

- 입력 장치를 마스터에서 분리:

`xinput float {{id}}`

- 입력 장치를 슬레이브로 마스터에 재연결:

`xinput reattach {{id}} {{마스터_id}}`

- 입력 장치의 설정 나열:

`xinput list-props {{id}}`

- 입력 장치의 설정 변경:

`xinput set-prop {{id}} {{설정_id}} {{값}}`
