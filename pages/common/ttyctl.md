# ttyctl

> Freeze or unfreeze the terminal (TTY) settings in Zsh.
> When frozen, external programs cannot alter terminal settings.
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- [f]reeze the terminal to prevent external programs from changing its settings:

`ttyctl -f`

- Unfreeze the terminal to allow changes to its settings:

`ttyctl -u`

- Report whether the terminal is currently frozen or not:

`ttyctl`
