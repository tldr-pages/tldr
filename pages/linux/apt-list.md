# apt list

> List packages.
> Note: Recommended to run `apt update` first to refresh local package index files.
> More information: <https://manned.org/apt.8>.

- List all available packages:

`apt list`

- List packages by name only (supports wildcards like *):

`apt list {{package}}`

- List installed packages:

`apt list {{[-i|--installed]}}`

- List upgradable packages:

`apt list {{[-u|--upgradable]}}`
