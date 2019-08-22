# reg export

> Export the specified sub keys and values into a file.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg-export>.

- Export all sub keys and values of a specific key:

`reg export {{key_name}} {{path/to/file.reg}}`

- Force overwriting of an existing file without prompt:

`reg export {{key_name}} {{path/to/file.reg}} /y`
