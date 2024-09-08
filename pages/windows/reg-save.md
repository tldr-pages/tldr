# reg save

> Save a registry key, its subkeys and values to a native `.hiv` file.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- Save a registry key, its subkeys and values to a specific file:

`reg save {{key_name}} {{path\to\file.hiv}}`

- Forcefully (assuming [y]es) overwrite an existing file:

`reg save {{key_name}} {{path\to\file.hiv}} /y`
