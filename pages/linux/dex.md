# dex

> DesktopEntry Execution is a program to generate and execute DesktopEntry files of the Application type.
> More information: <https://github.com/jceb/dex>.

- Perform an autostart/execute all programs in the autostart folders:

`dex --autostart`

- Perform an autostart/execute all programs in the specified folders:

`dex --autostart --search-paths {{path/to/directory}}:{{path/to/directory}}`

- Preview the programs would be executed in a regular autostart:

`dex --autostart --dry-run`

- Preview the programs would be executed in a GNOME specific autostart:

`dex --autostart --dry-run --environment GNOME`

- Preview the value of DesktopEntry property Name:

`dex --property Name {{path/to/file}}`

- Create a DesktopEntry for a program in the current directory:

`dex --create {{path/to/file}}`

- Execute a single program (with Terminal=true in the desktop file) in given terminal:

`dex --term {{terminal}} {{path/to/file}}`
