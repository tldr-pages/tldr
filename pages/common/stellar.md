# stellar

> Build, deploy, and interact with Stellar Soroban smart contracts and networks.
> More information: <https://developers.stellar.org/docs/tools/cli/stellar-cli>.

- Build a Soroban smart contract in the current workspace:

`stellar contract build`

- Optimize a compiled WebAssembly smart contract binary:

`stellar contract optimize --wasm {{path/to/contract.wasm}}`

- Generate a new keypair identity and fund it on the Stellar testnet:

`stellar keys generate {{identity_name}} {{[-n|--network]}} testnet --fund`

- Deploy a compiled smart contract to a network:

`stellar contract deploy --wasm {{path/to/contract.wasm}} {{[-s|--source]}} {{identity_name}} {{[-n|--network]}} {{testnet|mainnet}}`

- Invoke a function on a deployed smart contract:

`stellar contract invoke --id {{contract_id}} {{[-s|--source]}} {{identity_name}} {{[-n|--network]}} {{testnet|mainnet}} -- {{function_name}}`

- List configured Stellar networks:

`stellar network ls`

- Display version:

`stellar {{[-V|--version]}}`
