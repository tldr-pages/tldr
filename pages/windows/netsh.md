# netsh

> Manage Windows network settings.
> See also: `netsh wlan`.
> More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh>.

- Add a helper Dynamic Link Library (DLL):

`netsh add helper {{C:\\Path\\to\\file.dll}}`

- Show all loaded helper DLLs:

`netsh show helper`

- Delete a helper DLL:

`netsh delete helper {{C:\\Path\\to\\file.dll}}`

- Export your network configuration settings to a file:

`netsh dump > {{C:\\NetConfig\\netsh_config.txt}}`

- Show available network interfaces for tracing:

`netsh trace show interfaces`

- Exit the shell:

`exit`

- Display help:

`netsh help`
