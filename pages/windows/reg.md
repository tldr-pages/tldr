# reg

> Manage keys and their values in the Windows registry.
> Some subcommands such as `reg add` have their own usage documentation.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- Execute a registry command:

`reg {{command}}`

- View documentation for adding existing and new keys and subkeys:

`tldr reg {{add|copy|load}}`

- View documentation for deleting keys and subkeys:

`tldr reg {{delete|unload}}`

- View documentation for searching, viewing, and comparing keys:

`tldr reg {{compare|flags|query}}`

- View documentation for exporting and importing registry keys preserving the key ownerships and ACLs:

`tldr reg {{export|import}}`

- View documentation for saving and restoring registry keys not preserving the key ownerships and ACLs:

`tldr reg {{save|restore}}`

- Display help:

`reg /?`

- Display help for a specific command:

`reg {{command}} /?`
