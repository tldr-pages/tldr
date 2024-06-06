# hledger balance

> A flexible, general purpose "summing" report that shows accounts with some kind of numeric data.
> This can be balance changes per period, end balances, budget performance, unrealised capital gains, etc.
> More information: <https://hledger.org/hledger.html#balance>.

- Show the balance change in all accounts from all postings over all time:

`hledger balance`

- Show the balance change in accounts named `*expenses*`, as a tree, summarising the top two levels only:

`hledger balance {{expenses}} --tree --depth {{2}}`

- Show expenses each month, and their totals and averages, sorted by total; and their monthly budget goals:

`hledger balance {{expenses}} --monthly --row-total --average --sort-amount --budget`

- Similar to the above, shorter form, matching accounts by `Expense` type, as a two level tree without squashing boring accounts:

`hledger bal type:{{X}} -MTAS --budget -t -{{2}} --no-elide`

- Show end balances (including from postings before the start date), quarterly in 2024, in accounts named `*assets*` or `*liabilities*`:

`hledger balance --historical --period '{{quarterly in 2024}}' {{assets}} {{liabilities}}`

- Similar to the above, shorter form; also show zero balances, sort by total and summarise to three levels:

`hledger bal -HQ date:{{2024}} type:{{AL}} -ES -{{3}}`

- Show investment assets' market value in base currency at the end of each quarter:

`hledger bal -HVQ {{assets:investments}}`

- Show unrealised capital gains/losses from market price changes in each quarter, for non-cryptocurrency investment assets:

`hledger bal --gain -Q {{assets:investments}} not:{{cryptocurrency}}`
