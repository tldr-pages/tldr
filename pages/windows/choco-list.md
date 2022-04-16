# choco list

> Display a list of packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/list>.

- Print all packages matching the specified pattern:

`choco list {{pattern}}`

- Print all approved packages matching the specified pattern:

`choco list {{pattern}} --approved-only`

- Print all locally installed packages:

`choco list --local-only`

- Print all locally installed packages including local programs:

`choco list --local-only --include-programs`

- Print all packages from the specified source matching the given pattern:

`choco list --source {{source_url|source_alias}}`

- Provide a specific username and password for authentication:

`choco list --user {{username}} --password {{password}}`
