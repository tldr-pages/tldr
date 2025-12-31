# hledger balance

> A flexible, general purpose "summing" report that shows accounts with some kind of numeric data.
> This can be balance changes per period, end balances, budget performance, unrealised capital gains, etc.
> More information: <https://hledger.org/hledger.html#balance>.

- Show the balance change in all accounts from all postings over all time:

`hledger {{[bal|balance]}}`

- Show the balance change in accounts named `*expenses*`, as a tree, summarising the top two levels only:

`hledger {{[bal|balance]}} {{expenses}} {{[-t|--tree]}} {{[-2|--depth 2]}}`

- Show expenses each month, and their totals and averages, sorted by total; and their monthly budget goals:

`hledger {{[bal|balance]}} {{expenses}} {{[-M|--monthly]}} {{[-T|--row-total]}} {{[-A|--average]}} {{[-S|--sort-amount]}} --budget`

- Similar to the above, matching accounts by `Expense` type, as a two level tree without squashing boring accounts:

`hledger {{[bal|balance]}} type:{{X}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} --budget {{[-t|--tree]}} {{[-2|--depth 2]}} --no-elide`

- Show end balances (including from postings before the start date), quarterly in 2024, in accounts named `*assets*` or `*liabilities*`:

`hledger {{[bal|balance]}} {{[-H|--historical]}} {{[-p|--period]}} '{{quarterly in 2024}}' {{assets}} {{liabilities}}`

- Similar to the above, also show zero balances, sort by total and summarise to three levels:

`hledger {{[bal|balance]}} {{[-HQ|--historical --quarterly]}} date:{{2024}} type:{{AL}} {{[-ES|--empty --sort-amount]}} {{[-3|--depth 3]}}`

- Show investment assets' market [V]alue in base currency at the end of each quarter:

`hledger {{[bal|balance]}} {{[-HVQ|--historical --market --quarterly]}} {{assets:investments}}`

- Show unrealised capital gains/losses from market price changes in each quarter, for non-cryptocurrency investment assets:

`hledger {{[bal|balance]}} --gain {{[-Q|--quarterly]}} {{assets:investments}} not:{{cryptocurrency}}`
