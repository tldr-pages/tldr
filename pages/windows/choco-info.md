# choco info

> Display detailed information about a package with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/info>.

- Print information for the specified package:

`choco info {{package_name}}`

- Print information for the specified local package:

`choco info {{package_name}} --local-only`

- Get package information from the specified source:

`choco info {{package_name}} --source {{source_url|source_alias}}`

- Provide the username and the password for authentication:

`choco info {{package_name}} --user {{username}} --password {{password}}`
