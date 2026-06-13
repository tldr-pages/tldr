# kwallet-query

> Read and write to a KDE Wallet.
> More information: <https://manned.org/kwallet-query>.

- List all entries in the `Passwords` folder of `kdewallet`:

`kwallet-query {{kdewallet}} {{[-l|--list-entries]}}`

- List all entries in a specific folder:

`kwallet-query {{kdewallet}} {{[-l|--list-entries]}} {{[-f|--folder]}} {{folder_name}}`

- List all available folders:

`kwallet-query {{kdewallet}} {{[-l|--list-entries]}} {{[-f|--folder]}} ""`

- Display help:

`kwallet-query {{[-h|--help]}}`
