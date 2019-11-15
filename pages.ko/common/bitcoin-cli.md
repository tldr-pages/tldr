# bitcoin-cli

> RPC 호출을 통해 비트코인 데몬과 상호 작용하는 커맨드라인 클라이언트.`bitcoin.conf`에 정의된 구성 사용. 
> 자세한 정보:<https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- 지정된 주소로 트랜잭션 전송:

`bitcoin-cli sendtoaddress "{{address}}" {{amount}}`

- 하나 이상의 블록 생성:

`bitcoin-cli generate {{num_blocks}}`

- wallet에 대한 고급 정보 출력:

`bitcoin-cli getwalletinfo`

- 보내지지 않은 모든 트랜잭션의 출력 나열:

`bitcoin-cli listunspent`

- wallet 정보를 텍스트 파일로 출력:

`bitcoin-cli dumpwallet "{{path/to/file}}"`
