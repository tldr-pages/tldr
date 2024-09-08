# reg export

> Export the specified subkeys and values to a `.reg` file.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- Export all subkeys and values of a specific key:

`reg export {{key_name}} {{path\to\file.reg}}`

- Forcefully (assuming [y]es) overwrite of an existing file:

`reg export {{key_name}} {{path\to\file.reg}} /y`
