# Set-Service

> Starts, stops, and suspends a service, and changes its properties.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-service>.

- Change a display name:

`Set-Service -Name {{LanmanWorkstation}} -DisplayName {{"LanMan Workstation"}}`

- Change the startup type of services:

`Set-Service -Name {{BITS}} -StartupType {{Automatic}}`

- Change the description of a service:

`Set-Service -Name {{BITS}} -Description {{"Transfers files in the background using idle network bandwidth."}}`
