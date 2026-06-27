# wine reg add

> Add new keys and values to the Wine registry.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Add a new registry key:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}'`

- Add a [v]alue with specific [d]ata under a key:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /d {{data}}`

- Add a value with a specific data [t]ype (defaults to `REG_SZ`):

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /t {{REG_SZ|REG_DWORD|REG_QWORD|REG_BINARY|REG_MULTI_SZ|REG_EXPAND_SZ|REG_NONE}} /d {{data}}`

- Set the default (unnamed) value of a key:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /ve /d {{data}}`

- Add a `REG_MULTI_SZ` value, specifying the string [s]eparator character:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /t REG_MULTI_SZ /s {{#}} /d '{{string1#string2#string3}}'`

- [f]orcefully overwrite an existing value without prompting for confirmation:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /d {{data}} /f`

- Display help:

`wine reg add /?`
