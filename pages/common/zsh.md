# zsh

> Z SHell, a Bash-compatible command-line interpreter.
> See also: `bash`, `histexpand`.
> More information: <https://www.zsh.org>.

- Start an interactive shell session:

`zsh`

- Execute specific [c]ommands:

`zsh -c "{{echo Hello world}}"`

- Execute a specific script:

`zsh {{path/to/script.zsh}}`

- Check a specific script for syntax errors without executing it:

`zsh --no-exec {{path/to/script.zsh}}`

- Execute specific commands from stdin:

`{{echo Hello world}} | zsh`

- Execute a specific script, printing each command in the script before executing it:

`zsh --xtrace {{path/to/script.zsh}}`

- Start an interactive shell session in verbose mode, printing each command before executing it:

`zsh --verbose`

- Execute a specific command inside `zsh` with disabled glob patterns:

`noglob {{command}}`
