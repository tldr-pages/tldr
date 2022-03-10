# choco outdated

> Check for outdated packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/outdated>.

- Print all outdated packages in table format:

`choco outdated`

- Ignore pinned packages in the output:

`choco outdated --ignore-pinned`

- Check packages from the specified source:

`choco outdated --source {{source_url|alias}}`

- Provide the username and the password for authentication:

`choco outdated --user {{username}} --password {{password}}`
