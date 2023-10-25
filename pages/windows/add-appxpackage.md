# add-appxpackage

> A PowerShell utility to add a signed app package (`.appx`, `.msix`, `.appxbundle` and `.msixbundle`) to a user account.
> More information: <https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage>.

- Add an app package:

`add-appxpackage -Path {{path\to\package.msix}}`

- Add an app package with dependencies:

`add-appxpackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}}`

- Install an app using the app installer file:

`add-appxpackage -AppInstallerFile {{path\to\app.appinstaller}}`

- Add an unsigned package:

`add-appxpackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}} -AllowUnsigned`
