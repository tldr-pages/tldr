# sui client

> 스마트 계약을 배포하고, 객체 정보를 얻고, 트랜잭션을 실행하는 등의 작업을 수행합니다.
> 더 많은 정보: <https://docs.sui.io/references/cli/client>.

- ED25519 스키마로 새 주소 생성:

`sui client new-address ed25519 {{주소_별칭}}`

- RPC URL과 별칭으로 새 테스트넷 환경 생성:

`sui client new-env --rpc https://fullnode.testnet.sui.io:443 --alias testnet`

- 원하는 주소로 전환 (별칭도 허용):

`sui client switch --address {{주소_별칭}}`

- 지정된 환경으로 전환:

`sui client switch --env {{환경_별칭}}`

- 스마트 계약 배포:

`sui client publish {{패키지_경로}}`

- Sui 파셋과 상호작용:

`sui client faucet {{하위명령어}}`

- 지정된 주소의 가스 코인 나열 (별칭도 허용):

`sui client gas {{주소}}`

- 프로그래머블 트랜잭션 블록 생성, 서명 및 실행:

`sui client ptb {{옵션}} {{하위명령어}}`
