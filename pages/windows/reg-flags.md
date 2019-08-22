# reg flags

> Display or set flags on registry keys.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg-flags>.

- Display current flags for a specific key:

`reg flags {{key_name}} query`

- Display help and available flag types:

`reg flags /?`

- Set specified space-separated flags, and unset unmentioned flags, for a specific key:

`reg flags {{key_name}} set {{flag_names}}`

- Set specified flags for a specific key and its sub keys:

`reg flags {{key_name}} set {{flag_names}} /s`
