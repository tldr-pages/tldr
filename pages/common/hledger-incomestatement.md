# hledger incomestatement

> Show revenue inflows and expense outflows during the report period.
> Amounts are shown with normal positive sign, as in conventional financial statements.
> More information: <https://hledger.org/hledger.html#incomestatement>.

- Show revenues and expenses (changes in `Revenue` and `Expense` accounts):

`hledger {{[is|incomestatement]}}`

- Show revenues and expenses each month:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}}`

- Show monthly revenues/expenses/totals, largest first, summarised to 2 levels:

`hledger {{[is|incomestatement]}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} {{[-2|--depth 2]}}`

- Same as above, and generate HTML output in `is.html`:

`hledger {{[is|incomestatement]}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} {{[-2|--depth 2]}} {{[-o|--output-file]}} is.html`
