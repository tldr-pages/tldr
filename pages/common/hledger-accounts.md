# hledger accounts

> List account names.
> More information: <https://hledger.org/hledger.html#accounts>.

- Show all accounts used or declared in the default journal file:

`hledger {{[acc|accounts]}}`

- Show accounts used by transactions:

`hledger {{[acc|accounts]}} {{[-u|--used]}}`

- Show accounts declared with account directives:

`hledger {{[acc|accounts]}} {{[-d|--declared]}}`

- Add new account directives, for accounts used but not declared, to the journal:

`hledger {{[acc|accounts]}} --undeclared --directives >> {{2024-accounts.journal}}`

- Show accounts with `asset` in their name, and their declared/inferred types:

`hledger {{[acc|accounts]}} asset --types`

- Show accounts of the `Asset` type:

`hledger {{[acc|accounts]}} type:A`

- Show the first two levels of the accounts hierarchy:

`hledger {{[acc|accounts]}} {{[-t|--tree]}} {{[-2|--depth 2]}}`
