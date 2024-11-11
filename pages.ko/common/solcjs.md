# solcjs

> Solidity 컴파일러를 위한 JavaScript 바인딩 세트.
> 더 많은 정보: <https://github.com/ethereum/solc-js>.

- 특정 계약을 16진수로 컴파일:

`solcjs --bin {{경로/대상/파일.sol}}`

- 특정 계약의 ABI를 컴파일:

`solcjs --abi {{경로/대상/파일.sol}}`

- 가져오기를 해석할 기본 경로 지정:

`solcjs --bin --base-path {{경로/대상/폴더}} {{경로/대상/파일.sol}}`

- 외부 코드가 포함된 하나 이상의 경로 지정:

`solcjs --bin --include-path {{경로/대상/폴더}} {{경로/대상/파일.sol}}`

- 생성된 바이트코드 최적화:

`solcjs --bin --optimize {{경로/대상/파일.sol}}`
