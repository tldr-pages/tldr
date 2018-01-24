# reg flags

> Display or set flags on registry keys.

- Display current flags for a specific key:

`reg flags {{key_name}} query`

- Display help and available key types:

`reg flags /?`

- Set specified flags, and unset unmentioned flags, for a specific key:

`reg delete {{key_name}} set {{flag_names}}`

- Set specified flags for a specific key and its sub keys:

`reg delete {{key_name}} set {{flag_names}} /s`
