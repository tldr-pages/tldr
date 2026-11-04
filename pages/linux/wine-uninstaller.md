# wine uninstaller

> List and remove Windows applications installed in a Wine prefix.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Open the graphical "Add/Remove Programs" dialog:

`wine uninstaller`

- List all installed applications and their registry keys:

`wine uninstaller --list`

- Remove a specific application by its registry key:

`wine uninstaller --remove {{registry_key}}`

- Display help:

`wine uninstaller --help`
