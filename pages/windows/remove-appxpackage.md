# remove-appxpackage

> A PowerShell utility to remove an app package from one or more user accounts.
> More information: <https://learn.microsoft.com/powershell/module/appx/remove-appxpackage>.

- Remove an app package:

`remove-appxpackage {{package}}`

- Remove an app package for a specific user:

`remove-appxpackage {{package}} -User {{username}}`

- Remove an app package for all users:

`remove-appxpackage {{package}} -AllUsers`

- Remove an app package but preserve it's app data:

`remove-appxpackage {{package}} -PreserveApplicationData`
