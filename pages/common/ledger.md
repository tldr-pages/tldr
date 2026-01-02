# ledger

> A powerful, double-entry accounting system.
> More information: <https://ledger-cli.org/doc/ledger.1.html>.

- Print a balance report showing totals:

`ledger balance --file {{path/to/ledger.journal}}`

- List all postings in Expenses ordered by amount:

`ledger register {{expenses}} {{[-S|--sort]}} {{amount}}`

- Print total Expenses other than Drinks and Food:

`ledger balance {{Expenses}} and not ({{Drinks}} or {{Food}})`

- Print a budget report:

`ledger budget`

- Print summary information about all the postings:

`ledger stats`
