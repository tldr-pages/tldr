# Stop-Service

> Stops running services.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- Stop a service on the local computer:

`Stop-Service -Name {{service_name}}`

- Stop a service by using the display name:

`Stop-Service -DisplayName "{{name}}"`

- Stop a service that has dependent services:

`Stop-Service -Name {{service_name}} -Force -Confirm`
