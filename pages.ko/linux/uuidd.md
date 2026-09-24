# uuidd

> UUID 생성을 위한 데몬.
> 더 많은 정보: <https://manned.org/uuidd>.

- 무작위 UUID 생성:

`uuidd {{[-r|--random]}}`

- 다수의 무작위 UUID 생성:

`uuidd {{[-r|--random]}} {{[-n|--uuids]}} {{uuid_개수}}`

- 현재 시간과 시스템의 MAC 주소를 기반으로 한 시간 기반 UUID 생성:

`uuidd {{[-t|--time]}}`
