# reg compare

> Compare keys and their values in the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- Compare all values under a specific key with a second key:

`reg compare {{first_key_name}} {{second_key_name}}`

- Compare a specific value under two keys:

`reg compare {{first_key_name}} {{second_key_name}} /v {{value}}`

- Compare all sub keys and values for two keys:

`reg compare {{first_key_name}} {{second_key_name}} /s`

- Only output the matches between the specified keys:

`reg compare {{first_key_name}} {{second_key_name}} /os`

- Output the differences and matches between the specified keys:

`reg compare {{first_key_name}} {{second_key_name}} /oa`
