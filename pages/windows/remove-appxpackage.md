# Remove-AppxPackage

> A PowerShell utility to remove an app package from one or more user accounts.
> More information: <https://learn.microsoft.com/powershell/module/appx/Remove-AppxPackage>.

- Remove an app package:

`Remove-AppxPackage {{package}}`

- Remove an app package for a specific user:

`Remove-AppxPackage {{package}} -User {{username}}`

- Remove an app package for all users:

`Remove-AppxPackage {{package}} -AllUsers`

- Remove an app package but preserve it's app data:

`Remove-AppxPackage {{package}} -PreserveApplicationData`
