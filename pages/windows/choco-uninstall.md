# choco uninstall

> Uninstall one or more packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/uninstall>.

- Uninstall one or more specified packages:

`choco uninstall {{package_name1 package_name2 ...}}`

- Uninstall a specific version of a package:

`choco uninstall {{package_name}} --version {{package_version}}`

- Confirm all prompts automatically:

`choco uninstall {{package_name}} --yes`

- Remove all dependencies when uninstalling:

`choco uninstall {{package_name}} --remove-dependencies`

- Uninstall all packages:

`choco uninstall all`
