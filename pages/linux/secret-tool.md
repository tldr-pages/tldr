# secret-tool

> Store and retrieve passwords, part of the `libsecret` package.
> Communicates with `Secret Service` implementation such as `gnome-keyring`.
> For more information <https://wiki.gnome.org/Projects/Libsecret>.

- Store a secret with optional label:

`secret-tool store --label={{label}} {{key}} {{value}}`

- Retrieve a secret:

`secret-tool lookup key {{key}}`

- Get more information about secret:

`secret-tool search key {{key}}`

- Delete a stored secret:

`secret-tool clear key {{key}}`
