# apx pkgmanagers

> Manage package managers in `apx`.
> Note: User-created package manager configurations are stored in `~/.local/share/apx/pkgmanagers`.
> More information: <https://github.com/Vanilla-OS/apx>.

- Interactively create a new package manager configuration:

`apx pkgmanagers create`

- List all available package manager configurations:

`apx pkgmanagers list`

- Remove a package manager configuration:

`apx pkgmanagers rm --name {{string}}`

- Display information about a specific package manager:

`apx pkgmanagers show {{name}}`

- Update the configuration for a specific package manager (useful to change settings or sources):

`apx pkgmanagers update --name {{string}} --config {{path/to/config}}`

- Enable or disable a package manager configuration:

`apx pkgmanagers set-state --name {{string}} --state {{enabled|disabled}}`

- Validate all existing package manager configurations to check for errors:

`apx pkgmanagers validate`

- Export package manager configuration(s) for backup or sharing:

`apx pkgmanagers export --name {{string}} --output {{path/to/export}}`
