# hsd-cli

> Handshake 블록체인용 커멘드 라인 REST 도구.
> 더 많은 정보: <https://handshake.org>.

- 현재 서버에 대한 정보 검색:

`hsd-cli info`

- 로컬 트랜잭션 브로드캐스트:

`hsd-cli broadcast {{트랜잭션_16진수값}}`

- mempool 스냅샷 검색:

`hsd-cli mempool`

- 주소 또는 해시로 트랜잭션 보기:

`hsd-cli tx {{주소_또는_해시}}`

- 해시 인덱스 또는 주소로 코인 보기:

`hsd-cli coin {{해시_인덱스_또는_주소}}`

- 높이 또는 해시별로 블록 보기:

`hsd-cli block {{높이_또는_해시}}`

- 지정된 블록으로 체인을 재설정:

`hsd-cli reset {{높이_또는_해시}}`

- RPC 명령을 실행:

`hsd-cli rpc {{명령어}} {{인자}}`
