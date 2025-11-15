# bluetoothctl

> 블루투스 장치를 관리합니다.
> 더 많은 정보: <https://manned.org/bluetoothctl>.

- `bluetoothctl` 셸에 진입:

`bluetoothctl`

- 모든 알려진 장치 나열:

`bluetoothctl devices`

- 블루투스 컨트롤러를 켜거나 끔:

`bluetoothctl power {{on|off}}`

- 장치와 페어링:

`bluetoothctl pair {{맥_주소}}`

- 장치 제거:

`bluetoothctl remove {{맥_주소}}`

- 페어링된 장치에 연결:

`bluetoothctl connect {{맥_주소}}`

- 페어링된 장치와 연결 해제:

`bluetoothctl disconnect {{맥_주소}}`

- 도움말 표시:

`bluetoothctl help`
