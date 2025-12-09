# hsw-cli

> Handshake 지갑을 위한 커멘드 라인 REST 도구.
> 더 많은 정보: <https://github.com/handshake-org/hs-client>.

- 현재 지갑 잠금 해제 (초 단위 시간 초과):

`hsw-cli unlock {{암호}} {{시간}}`

- 현재 지갑을 잠금:

`hsw-cli lock`

- 현재 지갑의 세부정보 보기:

`hsw-cli get`

- 현재 지갑 잔액 보기:

`hsw-cli balance`

- 현재 지갑의 거래 내역 보기:

`hsw-cli history`

- 지정된 코인 금액으로 트랜잭션을 주소로 보냄:

`hsw-cli send {{주소}} {{1.05}}`

- 현재 지갑의 보류 중인 트랜잭션을 확인:

`hsw-cli pending`

- 트랜잭션 세부정보 보기:

`hsw-cli tx {{트랜잭션_해시}}`
