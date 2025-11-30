# unsetopt

> Unset options for the Z shell (zsh).
> To set options, use `setopt`.
> Note: Zsh options are case-insensitive and underscores are ignored.
> More information: <https://zsh.sourceforge.io/Doc/Release/Options.html>.

- List all currently unset options (use `setopt` to list set options):

`unsetopt`

- Unset a specific option:

`unsetopt {{option_name}}`

- Unset multiple options at once:

`unsetopt {{option_name1 option_name2 ...}}`
