# choco uninstall

> Uninstall one or more packages with Chocolatey.

- Uninstall one or more space-separated packages:

`choco uninstall {{package(s)}}`

- Uninstall a specific version of a package:

`choco uninstall {{package}} --version {{version}}`

- Confirm all prompts automatically:

`choco uninstall {{package}} --yes`

- Uninstall all versions of a package:

`choco uninstall {{package}} --all-versions`

- Remove all dependencies when uninstalling:

`choco uninstall {{package}} --remove-dependencies`

- Uninstall all packages:

`choco uninstall all`
