# hledger-ui

> A terminal interface (TUI) for `hledger`, a robust, friendly plain text accounting app.
> More information: <https://hledger.org/hledger-ui.html>.

- Start in the main menu screen, reading from the default journal file:

`hledger-ui`

- Start with a different color theme:

`hledger-ui --theme {{terminal|greenterm|dark}}`

- Start in the balance sheet accounts screen, showing hierarchy down to level 3:

`hledger-ui --bs --tree --depth 3`

- Start in this account's screen, showing cleared transactions, and reload on change:

`hledger-ui --register {{assets:bank:checking}} --cleared --watch`

- Read two journal files, and show amounts as current value when known:

`hledger-ui --file {{path/to/2024.journal}} --file {{path/to/2024-prices.journal}} --value now`

- Show the manual in Info format, if possible:

`hledger-ui --info`

- Display help:

`hledger-ui --help`
