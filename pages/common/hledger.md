# hledger

> A robust, friendly plain text accounting app.
> See also: `hledger-ui` for TUI, `hledger-web` for web interface.
> More information: <https://hledger.org/hledger.html>.

- Record new transactions interactively, saving to the default journal file:

`hledger add`

- Import new transactions from `bank.csv`, using `bank.csv.rules` to convert:

`hledger import {{path/to/bank.csv}}`

- Print all transactions, reading from multiple specified journal files:

`hledger print --file {{path/to/prices-2024.journal}} --file {{path/to/prices-2023.journal}}`

- Show all accounts, as a hierarchy, and their types:

`hledger accounts --tree --types`

- Show asset and liability account balances, including zeros, hierarchically:

`hledger balancesheet --empty --tree --no-elide`

- Show monthly incomes/expenses/totals, largest first, summarised to 2 levels:

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- Show the `assets:bank:checking` account's transactions and running balance:

`hledger aregister assets:bank:checking`

- Show the amount spent on food from the `assets:cash` account:

`hledger print assets:cash | hledger -f- -I aregister expenses:food`
