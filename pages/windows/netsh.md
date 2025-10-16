# netsh

> Command-line utility for managing  Windows network settings. Some commands require administrator privileges.
> More information: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh


- Show help and list all available contexts:

`netsh help` 


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


- Exit 'netsh' shell

`exit`


- For wireless network management commands, see:

`tldr netsh wlan`
