# Add-AppxPackage

> A PowerShell utility to add a signed app package (`.appx`, `.msix`, `.appxbundle` and `.msixbundle`) to a user account.
> More information: <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- Add an app package:

`Add-AppxPackage -Path {{path\to\package.msix}}`

- Add an app package with dependencies:

`Add-AppxPackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}}`

- Install an app using the app installer file:

`Add-AppxPackage -AppInstallerFile {{path\to\app.appinstaller}}`

- Add an unsigned package:

`Add-AppxPackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}} -AllowUnsigned`
