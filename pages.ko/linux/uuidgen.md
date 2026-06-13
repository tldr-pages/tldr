# uuidgen

> 고유 식별자(UUID)를 생성합니다.
> 관련 항목: `uuid`.
> 더 많은 정보: <https://manned.org/uuidgen>.

- 무작위 UUIDv4 생성:

`uuidgen {{[-r|--random]}}`

- 현재 시간을 기반으로 UUIDv1 생성:

`uuidgen {{[-t|--time]}}`

- 지정된 네임스페이스 접두사를 가진 이름의 UUIDv5 생성:

`uuidgen {{[-s|--sha1]}} {{[-n|--namespace]}} {{@dns|@url|@oid|@x500}} {{[-N|--name]}} {{객체_이름}}`
