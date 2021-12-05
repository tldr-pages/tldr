# zsh

> Z SHell, a Bash-compatible command-line interpreter.
> See also `histexpand` for history expansion.
> More information: <https://www.zsh.org>.

- Start an interactive shell session:

`zsh`

- Execute [c]ommands:

`zsh -c "echo 'zsh is executed'"`

- Execute a script:

`zsh {{path/to/script.zsh}}`

- Check a script for syntax errors:

`zsh --no-exec "{{path/to/script.zsh}}"`

- Execute a script while printing each command before executing it:

`zsh --xtrace {{path/to/script.zsh}}`

- Start an interactive shell session in verbose mode while printing each command before executing it:

`zsh --verbose`

- Print the version (`$ZSH_VERSION` contains the version without the license information):

`zsh --version`
