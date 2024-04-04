# reg flags

> Display or set flags on registry keys.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-flags>.

- Display current flags for a specific key:

`reg flags {{key_name}} query`

- Set one or more flags, and unset unmentioned flags, for a specific key:

`reg flags {{key_name}} set {{flag_name1 flag_name2 ...}}`

- Set one or more flags for a specific key and its [s]ubkeys:

`reg flags {{key_name}} set {{flag_name1 flag_name2 ...}} /s`
