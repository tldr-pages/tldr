# bindkey

> Add keybindings to Z-Shell.
> More information: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

- Bind a hotkey to a specific command:

`bindkey "{{^k}}" {{kill-line}}`

- Bind a hotkey to a specific key sequence:

`bindkey -s '^o' 'cd ..\n'`

- View keymaps:

`bindkey -l`

- View the hotkey in a keymap:

`bindkey -M main`
