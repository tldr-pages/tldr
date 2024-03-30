# bindkey

> Add keybindings to Z-Shell.
> More information: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

- Bind a hotkey to a specific command:

`bindkey "{{^k}}" {{kill-line}}`

- Bind a hotkey to a specific key [s]equence:

`bindkey -s '^o' 'cd ..\n'`

- [l]ist keymaps:

`bindkey -l`

- View the hotkey in a key[M]ap:

`bindkey -M main`
