# light-arionum-cli

> The PHP light wallet for the Arionum cryptocurrency.
> More information: <https://github.com/arionum/lightWalletCLI>.

- Generate a new public/private key pair:

`light-arionum-cli`

- Display the balance of the current address:

`light-arionum-cli balance`

- Display the balance of the specified address:

`light-arionum-cli balance {{address}}`

- Send a transaction with an optional message:

`light-arionum-cli send {{address}} {{value}} {{optional_message}}`

- Export the current wallet information:

`light-arionum-cli export`

- Display information about the current block:

`light-arionum-cli block`

- Display information about the current address' transactions:

`light-arionum-cli transactions`

- Display information about a specific transaction:

`light-arionum-cli transaction {{transaction_id}}`
