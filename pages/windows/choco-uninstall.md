# choco uninstall

> Uninstall packages with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-uninstall>.

- Uninstall one or more packages:

`choco uninstall {{package1 package2 ...}}`

- Uninstall a specific version of a package:

`choco uninstall {{package}} --version {{version}}`

- Confirm all prompts automatically:

`choco uninstall {{package}} --yes`

- Remove all dependencies when uninstalling:

`choco uninstall {{package}} --remove-dependencies`

- Uninstall all packages:

`choco uninstall all`
