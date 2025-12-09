# sui client ptb

> 프로그래머블 트랜잭션 블록 생성, 서명 및 실행.
> 더 많은 정보: <https://docs.sui.io/references/cli/ptb>.

- 패키지와 모듈에서 Move 함수 호출:

`sui client ptb --move-call p::m::f "<{{타입}}>" args`

- u64 타입의 두 요소로 Move 벡터 생성:

`sui client ptb --make-move-vec "<u64>" "[1000,2000]"`

- 가스 코인을 분할하고 주소로 전송:

`sui client ptb --split-coins gas "[1000]" --assign new_coins --transfer-objects "[new_coins]" @{{주소}}`

- 객체를 주소로 전송:

`sui client ptb --transfer-objects "[{{객체_ID}}]" @{{주소}}`

- Move 패키지를 게시하고 업그레이드 기능을 송신자에게 전송:

`sui client ptb --move-call sui::tx_context::sender --assign sender --publish "." --assign upgrade_cap --transfer-objects "[upgrade_cap]" sender`
