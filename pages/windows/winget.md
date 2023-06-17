# winget

> Windows Package Manager CLI.
> More information: <https://learn.microsoft.com/windows/package-manager/winget>.

- Install a package:

`winget install {{package}}`

- Remove a package (Note: `remove` can also be used instead of `uninstall`):

`winget uninstall {{package}}`

- Display information about a package:

`winget show {{package}}`

- Search for a package:

`winget search {{package}}`

- Upgrade all packages to the latest versions:

`winget upgrade --all`

- List all packages installed that can be managed with `winget`:

`winget list --source winget`

- Import packages from a file, or export installed packages to a file:

`winget {{import|export}} {{--import-file|--output}} {{path/to/file}}`

- Validate manifests before submitting a PR to the winget-pkgs repository:

`winget validate {{path/to/manifest}}`
