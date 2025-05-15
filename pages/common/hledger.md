# hledger

> A robust, friendly plain text accounting app.
> See also: `hledger-ui` for TUI, `hledger-web` for web interface.
> More information: <https://hledger.org/hledger.html>.

- Record new transactions interactively, saving to the default journal file:

`hledger add`

- Import new transactions from `bank.csv`, using `bank.csv.rules` to convert:

`hledger import {{path/to/bank.csv}}`

- Print all transactions, reading from multiple specified journal files:

`hledger print {{[-f|--file]}} {{path/to/prices-2024.journal}} {{[-f|--file]}} {{path/to/prices-2023.journal}}`

- Show all accounts, as a hierarchy, and their types:

`hledger accounts {{[-t|--tree]}} --types`

- Show asset and liability account balances, including zeros, hierarchically:

`hledger {{[bs|balancesheet]}} {{[-E|--empty]}} {{[-t|--tree]}} --no-elide`

- Show monthly incomes/expenses/totals, largest first, summarised to 2 levels:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}} {{[-T|--row-total]}} {{[-A|--average]}} --sort {{[-2|--depth 2]}}`

- Show the `assets:bank:checking` account's transactions and running balance:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Show the amount spent on food from the `assets:cash` account:

`hledger print assets:cash | hledger {{-f|--file}} - {{[-I|--ignore-assertions]}} aregister expenses:food`
