# choco

> The Chocolatey package manager for Windows.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/>.

- Install a package from the default Chocolatey repository and agree to prompts:

`choco install {{packageName}} -y`

- Upgrade a specific installed package to the latest version:

`choco upgrade {{packageName}} -y`

- Upgrade all outdated packages:

`choco upgrade all -y`

- Uninstall a package:

`choco uninstall {{packageName}} -y`

- Search for packages by name or keyword:

`choco search {{query}}`

- List all packages installed on the machine:

`choco list --local-only`

- Show packages that have newer versions available:

`choco outdated`

- Install a package from a local folder or private source:

`choco install {{packageName}} --source '{{path\to\folder_or_feed}}' -y`
