# octez-client

> Tezos 블록체인과 상호작용.
> 더 많은 정보: <https://tezos.gitlab.io/introduction/howtouse.html#client>.

- <https://rpc.ghostnet.teztnets.com>과 같은 Tezos RPC 노드에 연결하여 클라이언트 구성:

`octez-client -E {{엔드포인트}} config update`

- 계정을 생성하고 로컬 별칭을 지정:

`octez-client gen keys {{별칭}}`

- 별칭이나 주소로 계정의 잔액 확인:

`octez-client get balance for {{별칭_또는_주소}}`

- 다른 계정으로 tez 전송:

`octez-client transfer {{5}} from {{별칭|주소}} to {{별칭|주소}}`

- 스마트 계약 생성(배포), 로컬 별칭 지정 및 초기 저장소를 Michelson-인코딩된 값으로 설정:

`octez-client originate contract {{별칭}} transferring {{0}} from {{별칭|주소}} running {{경로/대상/소스_파일.tz}} --init "{{초기_저장소}}" --burn_cap {{1}}`

- 별칭이나 주소로 스마트 계약 호출 및 Michelson-인코딩된 매개변수 전달:

`octez-client transfer {{0}} from {{별칭|주소}} to {{계약}} --entrypoint "{{엔트리포인트}}" --arg "{{매개변수}}" --burn-cap {{1}}`

- 도움말 표시:

`octez-client man`
