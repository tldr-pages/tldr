# choco outdated

> Check for outdated packages with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-outdated>.

- Display a list of outdated packages in table format:

`choco outdated`

- Ignore pinned packages in the output:

`choco outdated --ignore-pinned`

- Specify a custom source to check packages from:

`choco outdated --source {{source_url|alias}}`

- Provide a username and password for authentication:

`choco outdated --user {{username}} --password {{password}}`
