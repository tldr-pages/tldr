# blkpr

> Persistent Reservations를 지원하는 블록 장치에서 예약을 등록, 예약, 해제, 선점 및 지우기.
> 더 많은 정보: <https://manned.org/blkpr>.

- 주어진 장치에 주어진 키로 새로운 예약을 등록 (명령)하기:

`blkpr {{-c|--command}} register {{[-k|--key]}} {{예약_키}} {{경로/대상/장치}}`

- 기존 예약의 유형을 배타적 접근으로 설정:

`blkpr {{[-c|--command]}} reserve {{[-k|--key]}} {{예약_키}} {{[-t|--type]}} exclusive-access {{경로/대상/장치}}`

- 주어진 키로 기존 예약을 선점하고 새로운 예약으로 교체:

`blkpr {{[-c|--command]}} preempt {{[-K|--oldkey]}} {{이전_키}} {{[-k|--key]}} {{새로운_키}} {{[-t|--type]}} write-exclusive {{경로/대상/장치}}`

- 주어진 장치에서 주어진 키와 유형으로 예약 해제:

`blkpr {{[-c|--command]}} release {{[-k|--key]}} {{예약_키}} {{[-t|--type]}} {{예약_유형}} {{경로/대상/장치}}`

- 주어진 장치에서 모든 예약 지우기:

`blkpr {{[-c|--command]}} clear {{[-k|--key]}} {{키}} {{경로/대상/장치}}`
