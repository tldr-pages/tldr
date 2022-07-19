# zsh

> Z SHell, a Bash-compatible command-line interpreter.
> See also `histexpand` for history expansion.
> More information: <https://www.zsh.org>.

- Start an interactive shell session:

`zsh`

- Execute a command and then exit:

`zsh -c "{{command}}"`

- Execute a script:

`zsh {{path/to/script.zsh}}`

- Execute a script, printing each command before executing it:

`zsh --xtrace {{path/to/script.zsh}}`

- Start an interactive shell session in verbose mode, printing each command before executing it:

`zsh --verbose`

- Execute a specific command inside `zsh` with disabled glob patterns:

`noglob {{command}}`
