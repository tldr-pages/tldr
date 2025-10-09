# choco

> The Chocolatey package manager.
> Some subcommands such as `install`, `upgrade`, `pin` have their own usage documentation.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/>.

- Install a package:

`choco install {{package_name}}`

- Upgrade a specific installed package:

`choco upgrade {{package_name}}`

- Upgrade all outdated packages and automatically confirm all prompts:

`choco upgrade all {{[-y|--yes]}}`

- Uninstall a package and automatically confirm all prompts:

`choco uninstall {{package_name}} {{[-y|--yes]}}`

- Search for packages by name or keyword:

`choco search {{query}}`

- List all packages installed on the machine:

`choco list`

- Show packages that have newer versions available:

`choco outdated`

- Install a package from a specific source:

`choco install {{package_name}} {{[-s|--source]}} {{source}}`
