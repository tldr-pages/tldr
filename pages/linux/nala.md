# nala

> Package management Utility.
> Wrapper for the `apt` package manager.
> More information: <https://gitlab.com/volian/nala>.

- Install a package, or update it to the latest available version:

`nala install {{package}}`

- Remove a package:

`sudo nala remove {{package}}`

- Remove a package and its configuration files:

`nala purge {{package}}`

- Search package names and descriptions using a word, regex (default) or glob:

`sudo nala search "{{pattern}}"`

- Update the list of available packages and upgrade the system:

`nala upgrade`

- Remove all unused packages and dependencies from your system:

`nala autoremove`

- Fetch fast mirrors to improve download speeds:

`nala fetch`

- Display the history of all transactions:

`nala history`
