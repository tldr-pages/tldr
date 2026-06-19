# wine reg

> Manage keys and their values in the Wine registry.
> Some subcommands such as `add`, `delete`, `query`, etc. have their own usage documentation.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Add or overwrite a value under a key (creating the key if needed):

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /d {{data}} /f`

- Display the values stored under a key:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}'`

- Delete a value from a key:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /f`

- Copy a key and all its subkeys to a new location:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /s`

- Export a key and its subkeys to a `.reg` file:

`wine reg export '{{HKEY_CURRENT_USER\path\to\key}}' {{path/to/file.reg}}`

- Import registry entries from a `.reg` file:

`wine reg import {{path/to/file.reg}}`

- Display help:

`wine reg /?`
