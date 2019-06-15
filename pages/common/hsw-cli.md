# hsw-cli

> The command line REST tool for the Handshake wallet.
> More information: <https://npmjs.com/package/hs-client>.

- Unlock the current wallet:

`hsw-cli unlock {{passphrase}} {{timeout}}`

- Lock the current wallet:

`hsw-cli lock`

- View the current wallets details:

`hsw-cli get`

- View the current wallets balance:

`hsw-cli balance`

- View the current wallets transaction history:

`hsw-cli history`

- Send a transaction to the specified address:

`hsw-cli send {{address}} {{value}}`

- View the current wallets pending transactions:

`hsw-cli pending`

- View details about a transaction:

`hsw-cli tx {{transaction_hash}}`
