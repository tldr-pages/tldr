# dex

> DesktopEntry Execution is a program to generate and execute DesktopEntry files of the Application type.
> More information: <https://github.com/jceb/dex#dex>.

- Execute all programs in the autostart folders:

`dex {{[-a|--autostart]}}`

- Execute all programs in the specified folders:

`dex {{[-a|--autostart]}} {{[-s|--search-paths]}} {{path/to/directory1}}:{{path/to/directory2}}:{{path/to/directory3}}:`

- Preview the programs would be executed in a GNOME specific autostart:

`dex {{[-a|--autostart]}} {{[-e|--environment]}} {{GNOME}}`

- Preview the programs would be executed in a regular autostart:

`dex {{[-a|--autostart]}} {{[-d|--dry-run]}}`

- Preview the value of the DesktopEntry property `Name`:

`dex {{[-p|--property]}} {{Name}} {{path/to/file.desktop}}`

- Create a DesktopEntry for a program in the current directory:

`dex {{[-c|--create]}} {{path/to/file.desktop}}`

- Execute a single program (with `Terminal=true` in the desktop file) in the given terminal:

`dex --term {{terminal}} {{path/to/file.desktop}}`
