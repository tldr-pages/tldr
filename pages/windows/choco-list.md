# choco list

> Display a list of packages with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-list>.

- Display all available packages:

`choco list`

- Display all locally installed packages:

`choco list --local-only`

- Display a list including local programs:

`choco list --include-programs`

- Display only approved packages:

`choco list --approved-only`

- Specify a custom source to display packages from:

`choco list --source {{source_url|alias}}`

- Provide a username and password for authentication:

`choco list --user {{username}} --password {{password}}`
