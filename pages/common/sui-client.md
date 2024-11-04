# sui client

> Publish smart contracts, get object information, execute transactions, and more.
> More information: <https://docs.sui.io/references/cli/client>.

- Create a new address with the ED25519 scheme:

`sui client new-address ed25519 {{address-alias}}`

- Create a new testnet environment with an RPC URL and alias:

`sui client new-env --rpc https://fullnode.testnet.sui.io:443 --alias testnet`

- Switch to the address of your choice (accepts also an alias):

`sui client switch --address {{address-alias}}`

- Switch to the given environment:

`sui client switch --env {{env-alias}}`

- Publish a smart contract:

`sui client publish {{package-path}}`

- Interact with the Sui faucet:

`sui client faucet {{subcommand}}`

- List the gas coins for the given address (accepts also an alias):

`sui client gas {{address}}`

- Create, sign, and execute programmable transaction blocks:

`sui client ptb {{options}} {{subcommand}}`
