# dex

> DesktopEntry Execution is a program to generate and execute DesktopEntry files of the Application type.
> More information: <https://github.com/jceb/dex>.

- Perform an autostart/execute all programs in the autostart folders:

`dex -a`

- Perform an autostart/execute all programs in the specified folders:

`dex -a -s {{path/to/directory}}:{{path/to/directory}}`

- Preview the programs would be executed in a regular autostart:

`dex -ad`

- Preview the programs would be executed in a GNOME specific autostart:

`dex -ad -e GNOME`

- Preview the value of DesktopEntry property Name:

`dex -p Name {{path/to/file}}`

- Create a DesktopEntry for a program in the current directory:

`dex -c {{path/to/file}}`

- Execute a single program (with Terminal=true in the desktop file) in given terminal:

`dex --term {{terminal}} {{path/to/file}}`
