# choco info

> Display detailed information about a package with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-info>.

- Display information on a specific package:

`choco info {{package}}`

- Display information for a local package only:

`choco info {{package}} {{[-l|--local-only]}}`

- Specify a custom source to receive packages information from:

`choco info {{package}} {{[-s|--source]}} {{source_url|alias}}`

- Provide a username and password for authentication:

`choco info {{package}} {{[-u|--user]}} {{username}} {{[-p|--password]}} {{password}}`
