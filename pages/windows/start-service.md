# Start-Service

> Starts one or more stopped services.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-service>.

- Start a service by using its name:

`Start-Service -Name {{"eventlog"}}`

- Display information without starting a service:

`Start-Service -DisplayName {{*remote*}} -WhatIf`

- Start a disabled service:

`Set-Service {{<service_name>}} -StartupType {{manual}}; Start-Service {{<service_name>}}`
