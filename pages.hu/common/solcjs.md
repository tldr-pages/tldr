# solcjs

> Egy sor JavaScript kötés a Solidity fordítóhoz. További információ: <https://github.com/ethereum/solc-js>.

- Egy adott szerződés fordítása hexára:

`solcjs --bin {{path/to/file.sol}}`

- Egy adott szerződés ABI-jének lefordítása:

`solcjs --abi {{path/to/file.sol}}`

- Adjon meg egy bázis elérési utat az importok feloldásához:

`solcjs --bin --base-path {{path/to/directory}} {{path/to/file.sol}}`

- Adjon meg egy vagy több elérési utat a külső kódot tartalmazó beépítéshez:

`solcjs --bin --include-path {{path/to/directory}} {{path/to/file.sol}}`

- A generált bájtkód optimalizálása:

`solcjs --bin --optimize {{path/to/file.sol}}`
