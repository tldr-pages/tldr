# zsh

> Z SHell, a Bash-compatible command-line interpreter.
> See also: `bash`, `!`, `^`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation>.

- Start an interactive shell session:

`zsh`

- Execute specific [c]ommands:

`zsh -c "{{echo Hello world}}"`

- Execute a specific script:

`zsh {{path/to/script.zsh}}`

- Check a specific script for syntax errors without executing it:

`zsh {{[-n|--no-exec]}} {{path/to/script.zsh}}`

- Execute specific commands from `stdin`:

`{{echo Hello world}} | zsh`

- Execute a specific script, printing each command in the script before executing it:

`zsh {{[-x|--xtrace]}} {{path/to/script.zsh}}`

- Start an interactive shell session in verbose mode, printing each command before executing it:

`zsh {{[-v|--verbose]}}`

- Start Zsh without loading user level configuration (e.g. `~/.zshrc`):

`zsh {{[-f|--no-rcs]}}`
