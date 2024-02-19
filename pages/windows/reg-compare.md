# reg compare

> Compare keys and their values in the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- Compare all values under a specific key with another key:

`reg compare {{key_name1}} {{key_name2}}`

- Compare a specific value under two keys:

`reg compare {{key_name1}} {{key_name2}} /v {{value}}`

- Compare all sub keys and values for two keys:

`reg compare {{key_name1}} {{key_name2}} /s`

- Only output the matches between the specified keys:

`reg compare {{key_name1}} {{key_name2}} /os`

- Output the differences and matches between the specified keys:

`reg compare {{key_name1}} {{key_name2}} /oa`
