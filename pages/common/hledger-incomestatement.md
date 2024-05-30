# hledger incomestatement

> Show revenue inflows and expense outflows during the report period.
> Amounts are shown with normal positive sign, as in conventional financial statements.
> More information: <https://hledger.org/hledger.html#incomestatement>.

- Show revenues and expenses (changes in `Revenue` and `Expense` accounts):

`hledger incomestatement`

- Show revenues and expenses each month:

`hledger incomestatement --monthly`

- Show monthly revenues/expenses/totals, largest first, summarised to 2 levels:

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- Short form of the above, and generate HTML output in `is.html`:

`hledger is -MTAS -2 -o is.html`
