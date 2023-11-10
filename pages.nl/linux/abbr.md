# abbr

> Beheer afkortingen voor de fish shell.
> User-defined words are replaced with longer phrases after they are entered.
> More information: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Voeg een nieuwe afkorting toe:

`abbr --add {{abbreviation_name}} {{command}} {{command_arguments}}`

- Hernoem een bestaande afkorting:

`abbr --rename {{old_name}} {{new_name}}`

- Wis een bestaande afkorting:

`abbr --erase {{abbreviation_name}}`

- Import the abbreviations defined on another host over SSH:

`ssh {{host_name}} abbr --show | source`
