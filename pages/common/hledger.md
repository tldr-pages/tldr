# hledger

> A plain text accounting software for the command-line.
> More information: <https://hledger.org>.

- Add transactions to your journal interactively:

`hledger add`

- Show the account hierarchy, using a specific journal file:

`hledger --file {{path/to/file.journal}} accounts --tree`

- Show a monthly income statement:

`hledger incomestatement --monthly --depth 2`

- Print the amount of cash spent on food:

`hledger print assets:cash | hledger -f- -I balance expenses:food --depth 2`
