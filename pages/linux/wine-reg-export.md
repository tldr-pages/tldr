# wine reg export

> Export keys, values, and data from the Wine registry to a `.reg` file.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Export a registry key and its subkeys to a file:

`wine reg export '{{HKEY_CURRENT_USER\path\to\key}}' {{path/to/file.reg}}`

- Export an entire registry hive to a file:

`wine reg export {{HKEY_CURRENT_USER}} {{path/to/file.reg}}`

- Overwrite the output file if it already exists, without prompting:

`wine reg export '{{HKEY_CURRENT_USER\path\to\key}}' {{path/to/file.reg}} /y`

- Display help:

`wine reg export /?`
