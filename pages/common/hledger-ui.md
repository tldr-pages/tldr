# hledger-ui

> A robust, friendly plain text accounting app (the terminal UI).
> More information: <https://hledger.org>.

- Start in the main menu screen, reading from the default journal file:

`hledger-ui`

- Start with a different color theme:

`hledger-ui --theme dark`

- Start in the balance sheet accounts screen, showing hierarchy, to level 3:

`hledger-ui --bs --tree --depth 3`

- Start in this account's screen, showing cleared txns, and reload on change:

`hledger-ui --register assets:bank:checking --cleared --watch`

- Read two journal files, and show amounts as current value when known:

`hledger-ui --file 2024.journal --file 2024-prices.journal --value now`

- Show command-line help:

`hledger-ui --help`

- Show the manual in Info format if possible:

`hledger-ui --info`
