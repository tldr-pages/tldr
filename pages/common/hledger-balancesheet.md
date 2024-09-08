# hledger balancesheet

> Show the end balances in asset and liability accounts.
> Amounts are shown with normal positive sign, as in conventional financial statements.
> More information: <https://hledger.org/hledger.html#balancesheet>.

- Show the current balances in `Asset` and `Liability` accounts, excluding zeros:

`hledger balancesheet`

- Show just the liquid assets (`Cash` account type):

`hledger balancesheet type:C`

- Include accounts with zero balances, and show the account hierarchy:

`hledger balancesheet --empty --tree`

- Show the balances at the end of each month:

`hledger balancesheet --monthly`

- Show the balances' market value in home currency at the end of each month:

`hledger balancesheet --monthly -V`

- Show quarterly balances, with just the top two levels of account hierarchy:

`hledger balancesheet --quarterly --tree --depth 2`

- Short form of the above, and generate HTML output in `bs.html`:

`hledger bs -Qt -2 -o bs.html`
