# reg query

> Display the values of keys and subkeys in the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- Display all values of a key:

`reg query {{key_name}}`

- Display a specific [v]alue of a key:

`reg query {{key_name}} /v {{value}}`

- Display all values of a key and its [s]ubkeys:

`reg query {{key_name}} /s`

- Search [f]or keys and values matching a specific pattern:

`reg query {{key_name}} /f "{{query_pattern}}"`

- Display a value of a key matching a specified data [t]ype:

`reg query {{key_name}} /t REG_{{SZ|MULTI_SZ|EXPAND_SZ|DWORD|BINARY|NONE}}`

- Only search in [d]ata:

`reg query {{key_name}} /d`

- Only search in [k]ey names:

`reg query {{key_name}} /f "{{query_pattern}}" /k`

- [c]ase-sensitively search for an [e]xact match:

`reg query {{key_name}} /c /e`
