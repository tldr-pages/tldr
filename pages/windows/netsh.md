# netsh

> Manage Windows network settings.
> Some subcommands such as `wlan` have their own usage documentation.
> More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh>.

- Add a helper Dynamic Link Library (DLL):

`netsh add helper {{path\to\file.dll}}`

- Show all loaded helper DLLs:

`netsh show helper`

- Delete a helper DLL:

`netsh delete helper {{path\to\file.dll}}`

- Export your network configuration settings to a file:

`netsh dump > {{path\to\output_file.txt}}`

- Show available network interfaces for tracing:

`netsh trace show interfaces`

- Exit the shell:

`exit`

- Display help:

`netsh help`
