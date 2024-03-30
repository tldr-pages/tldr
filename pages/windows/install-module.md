# Install-Module

> Install PowerShell modules from PowerShell Gallery, NuGet, and other repositories.
> More information: <https://learn.microsoft.com/powershell/module/powershellget/install-module>.

- Install a module, or update it to the latest available version:

`Install-Module {{module}}`

- Install a module with a specific version:

`Install-Module {{module}} -RequiredVersion {{version}}`

- Install a module no earlier than a specific version:

`Install-Module {{module}} -MinimumVersion {{version}}`

- Specify a range of supported versions (inclusive) of the required module:

`Install-Module {{module}} -MinimumVersion {{minimum_version}} -MaximumVersion {{maximum_version}}`

- Install module from a specific repository:

`Install-Module {{module}} -Repository {{repository}}`

- Install module from specific repositories:

`Install-Module {{module}} -Repository {{repository1 , repository2 , ...}}`

- Install the module for all/current user:

`Install-Module {{module}} -Scope {{AllUsers|CurrentUser}}`

- Perform a dry run to determine which modules will be installed, upgraded, or removed through `Install-Module`:

`Install-Module {{module}} -WhatIf`
