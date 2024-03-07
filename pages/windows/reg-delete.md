# reg delete

> Delete keys or their values from the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- Delete a specific registry key:

`reg delete {{key_name}}`

- Delete a [v]alue under a specific key:

`reg delete {{key_name}} /v {{value}}`

- Delete [a]ll [v]alues recursively under the specified key:

`reg delete {{key_name}} /va`

- [f]orcefully (without a prompt) delete [a]ll [v]alues recursively under a key:

`reg delete {{key_name}} /f /va`
