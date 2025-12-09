# reg add

> Add new keys and their values to the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- Add a new registry key:

`reg add {{key_name}}`

- Add a new [v]alue under a specific key:

`reg add {{key_name}} /v {{value}}`

- Add a new value with specific [d]ata:

`reg add {{key_name}} /d {{data}}`

- Add a new value to a key with a specific data [t]ype:

`reg add {{key_name}} /t REG_{{SZ|MULTI_SZ|DWORD_BIG_ENDIAN|DWORD|BINARY|DWORD_LITTLE_ENDIAN|LINK|FULL_RESOURCE_DESCRIPTOR|EXPAND_SZ}}`

- [f]orcefully (without a prompt) overwrite the existing registry value:

`reg add {{key_name}} /f`
