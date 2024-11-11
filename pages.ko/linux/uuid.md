# uuid

> 범용 고유 식별자(UUID) 생성 및 디코드.
> 같이 보기: `uuidgen`.
> 더 많은 정보: <https://manned.org/uuid>.

- UUIDv1 생성 (시간 및 시스템의 하드웨어 주소 기반, 사용 가능한 경우):

`uuid`

- UUIDv4 생성 (무작위 데이터 기반):

`uuid -v {{4}}`

- 여러 개의 UUIDv4를 한 번에 생성:

`uuid -v {{4}} -n {{UUID_개수}}`

- UUIDv4를 생성하고 출력 형식 지정:

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- UUIDv4를 생성하고 출력을 파일에 저장:

`uuid -v {{4}} -o {{경로/대상/파일}}`

- 주어진 네임스페이스 접두사로 UUIDv5 생성 (제공된 객체 이름 기반):

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{객체_이름}}`

- 주어진 UUID 디코드:

`uuid -d {{uuid}}`
