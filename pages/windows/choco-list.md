# choco list

> Display a list of packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/list>.

- Print packages matching the specified pattern:

`choco list {{pattern}}`

- Print approved packages matching the specified pattern:

`choco list {{pattern}} --approved-only`

- Print locally installed packages:

`choco list --local-only`

- Print locally installed packages including local programs:

`choco list --local-only --include-programs`

- Print packages from the specified source matching the given pattern:

`choco list --source {{source_url|alias}}`

- Provide the username and the password for authentication:

`choco list --user {{username}} --password {{password}}`
