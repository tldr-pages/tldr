# ledger

> Ledger is a powerful, double-entry accounting system that is accessed from the UNIX command-line.
> More information: <https://www.ledger-cli.org>.

- Print a balance report showing totals:

`ledger balance --file {{path/to/ledger.journal}}`

- List all postings in Expenses ordered by amount:

`ledger register {{expenses}} --sorted {{amount}}`

- Print total Expenses other than Drinks and Food:

`ledger balance {{Expenses}} and not ({{Drinks}} or {{Food}})`

- Print a budget report:

`ledger budget`

- Print summary information about all the postings:

`ledger stats`
