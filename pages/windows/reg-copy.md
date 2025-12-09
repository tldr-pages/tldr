# reg copy

> Copy keys and their values in the registry.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- Copy a registry key to a new registry location:

`reg copy {{old_key_name}} {{new_key_name}}`

- Copy a registry key recursively (with all [s]ubkeys) to a new registry location:

`reg copy {{old_key_name}} {{new_key_name}} /s`

- [f]orcefully (without a prompt) copy a registry key:

`reg copy {{old_key_name}} {{new_key_name}} /f`
