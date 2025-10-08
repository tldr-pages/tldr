# choco

> The Chocolatey package manager for Windows.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/>.

- Install a package:

`choco install {{package_name}} -y`

- Upgrade a specific package:

`choco upgrade {{package_name}} -y`

- Upgrade all packages:

`choco upgrade all -y`

- Uninstall a package:

`choco uninstall {{package_name}} -y`

- Search for packages:

`choco search {{query}}`

- List installed packages:

`choco list --local-only`

- Show outdated packages:

`choco outdated`

- Install a package from a local source:

`choco install {{package_name}} --source '{{path\to\source}}' -y`
