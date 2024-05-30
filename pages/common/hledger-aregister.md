# hledger aregister

> Show the transactions and running balances in one account, with each transaction on one line.
> More information: <https://hledger.org/hledger.html#aregister>.

- Show transactions and running balance in the `assets:bank:checking` account:

`hledger aregister assets:bank:checking`

- Show transactions and running balance in the first account named `*savings*`:

`hledger aregister savings`

- Show the checking account's cleared transactions, with a specified width:

`hledger aregister checking --cleared --width {{120}}`

- Show the checking register, including transactions from forecast rules:

`hledger aregister checking --forecast`
