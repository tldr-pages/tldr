# choco upgrade

> Upgrade one or more packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/upgrade>.

- Upgrade one or more specified packages:

`choco upgrade {{package_name1 package_name2 ...}}`

- Upgrade to the specified version of the package:

`choco upgrade {{package_name}} --version {{package_version}}`

- Upgrade all except specified comma-separated packages:

`choco upgrade all --except {{package_name1 package_name2 ...}}`

- Upgrade all packages:

`choco upgrade all`

- Confirm all prompts automatically:

`choco upgrade {{package_name}} --yes`

- Upgrade package from the specified source:

`choco upgrade {{package_name}} --source {{source_url|source_alias}}`

- Provide the username and the password for authentication:

`choco upgrade {{package_name}} --user {{username}} --password {{password}}`
