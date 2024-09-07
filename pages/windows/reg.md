# reg

> Manage keys and their values in the Windows registry.
> Some subcommands such as `reg add` have their own usage documentation.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- Execute a registry command:

`reg {{command}}`

- View documentation for adding and copying subkeys:

`tldr reg {{add|copy}}`

- View documentation for deleting keys and subkeys:

`tldr reg {{delete|unload}}`

- View documentation for searching, viewing, and comparing keys:

`tldr reg {{compare|flags|query}}`

- View documentation for exporting and importing registry keys not preserving the key ownerships and ACLs:

`tldr reg {{export|import}}`

- View documentation for saving, restoring registry and unloading keys preserving the key ownerships and ACLs:

`tldr reg {{save|restore|load|unload}}`

- Display help:

`reg /?`

- Display help for a specific command:

`reg {{command}} /?`
