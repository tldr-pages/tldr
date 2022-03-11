# abbr

> Manage abbreviations for the fish shell.
> User-defined words are replaced with longer phrases after they are entered.
> More information: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Add a new abbreviation:

`abbr --add {{abbreviation_name}} {{command}} {{command_arguments}}`

- Rename an existing abbreviation:

`abbr --rename {{old_name}} {{new_name}}`

- Erase an existing abbreviation:

`abbr --erase {{abbreviation_name}}`

- Import the abbreviations defined on another host over SSH:

`ssh {{host_name}} abbr --show | source`
