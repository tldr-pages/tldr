# reg compare

> Compare keys and their values in the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- Compare all values under a specific key with another key:

`reg compare {{key_name1}} {{key_name2}}`

- Compare a specific [v]alue under two keys:

`reg compare {{key_name1}} {{key_name2}} /v {{value}}`

- Compare all [s]ubkeys and values for two keys:

`reg compare {{key_name1}} {{key_name2}} /s`

- Only [o]utput the matches ([s]ame) between the specified keys:

`reg compare {{key_name1}} {{key_name2}} /os`

- [o]utput the differences and matches ([a]ll) between the specified keys:

`reg compare {{key_name1}} {{key_name2}} /oa`

- Compare two keys, [o]utputting [n]othing:

`reg compare {{key_name1}} {{key_name2}} /on`
