# hardhat

> Ethereum 소프트웨어 개발 환경.
> 더 많은 정보: <https://hardhat.org/hardhat-runner/docs/getting-started#quick-start>.

- 사용 가능한 하위 명령어를 나열 (또는 구성 파일이 없는 경우, 새로운 프로젝트 생성):

`hardhat`

- 현재 프로젝트를 컴파일하고, 모든 아티팩트를 빌드:

`hardhat compile`

- 프로젝트를 컴파일한 후 사용자 정의 스크립트를 실행:

`hardhat run {{경로/대상/스크립트.js}}`

- Mocha 테스트 실행:

`hardhat test`

- 주어진 모든 테스트 파일을 실행:

`hardhat test {{경로/대상/파일1.js}} {{경로/대상/파일2.js}}`

- 개발을 위해 로컬 Ethereum JSON-RPC 노드를 시작:

`hardhat node`

- 특정 호스트 이름과 포트를 사용하여 로컬 Ethereum JSON-RPC 노드를 시작:

`hardhat node --hostname {{호스트명}} --port {{포트}}`

- 캐시 및 모든 아티팩트 정리:

`hardhat clean`
