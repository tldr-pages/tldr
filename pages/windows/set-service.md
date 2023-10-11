# Set-Service

> Starts, stops, and suspends a service, and changes its properties.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- Change a display name:

`Set-Service -Name {{hostname}} -DisplayName "{{name}}"`

- Change the startup type of services:

`Set-Service -Name {{service_name}} -StartupType {{Automatic}}`

- Change the description of a service:

`Set-Service -Name {{service_name}} -Description "{{description}}"`
