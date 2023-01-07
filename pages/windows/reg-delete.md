# reg delete

> Delete keys or their values from the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- Delete a specific registry key:

`reg delete {{key_name}}`

- Delete a value under a specific key:

`reg delete {{key_name}} /v {{value}}`

- Delete all values recursively under the specified key:

`reg delete {{key_name}} /va`

- Forcefully delete all values recursively under a key without a prompt:

`reg delete {{key_name}} /f /va`
