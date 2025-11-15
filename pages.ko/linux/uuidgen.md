# uuidgen

> 고유 식별자(UUID)를 생성합니다.
> 같이 보기: `uuid`.
> 더 많은 정보: <https://manned.org/uuidgen>.

- 무작위 UUIDv4 생성:

`uuidgen --random`

- 현재 시간을 기반으로 UUIDv1 생성:

`uuidgen --time`

- 지정된 네임스페이스 접두사를 가진 이름의 UUIDv5 생성:

`uuidgen --sha1 --namespace {{@dns|@url|@oid|@x500}} --name {{객체_이름}}`
