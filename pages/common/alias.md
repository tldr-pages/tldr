# alias

> Create aliases - words that are replaced by a command string.
> Aliases expire with the current shell session unless defined in the shell's configuration file, e.g. `~/.bashrc` for Bash or `~/.zshrc` for Zsh.
> See also: `unalias`.
> More information: <https://manned.org/alias>.

- List all aliases:

`alias`

- Create a generic alias:

`alias {{word}}="{{command}}"`

- View the command associated to a given alias:

`alias {{word}}`

- Remove an aliased command:

`unalias {{word}}`

- Turn `rm` into an interactive command:

`alias {{rm}}="{{rm --interactive}}"`

- Create `la` as a shortcut for `ls --all`:

`alias {{la}}="{{ls --all}}"`
