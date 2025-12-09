# hledger aregister

> Show the transactions and running balances in one account, with each transaction on one line.
> More information: <https://hledger.org/hledger.html#aregister>.

- Show transactions and running balance in the `assets:bank:checking` account:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Show transactions and running balance in the first account named `*savings*`:

`hledger {{[areg|aregister]}} savings`

- Show the checking account's cleared transactions, with a specified width:

`hledger {{[areg|aregister]}} checking {{[-C|--cleared]}} {{[-w|--width]}} {{120}}`

- Show the checking register, including transactions from forecast rules:

`hledger {{[areg|aregister]}} checking --forecast`
