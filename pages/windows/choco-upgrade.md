# choco upgrade

> Upgrade one or more packages with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-upgrade>.

- Upgrade one or more space-separated packages:

`choco upgrade {{package(s)}}`

- Upgrade to a specific version of a package:

`choco upgrade {{package}} --version {{version}}`

- Upgrade all packages:

`choco upgrade all`

- Upgrade all except specified comma-separated packages:

`choco upgrade all --except "{{package(s)}}"`

- Confirm all prompts automatically:

`choco upgrade {{package}} --yes`

- Specify a custom source to receive packages from:

`choco upgrade {{package}} --source {{source_url|alias}}`

- Provide a username and password for authentication:

`choco upgrade {{package}} --user {{username}} --password {{password}}`
