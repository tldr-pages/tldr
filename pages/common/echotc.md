# echotc

> Output termcap terminal capability codes in Zsh.
> Part of the `zsh/termcap` module.
> See also: `echoti`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html#The-zsh_002ftermcap-Module>.

- Load the termcap module before use:

`zmodload zsh/termcap`

- Move the cursor to the beginning of the line:

`echotc cr`

- Clear the screen:

`echotc cl`

- Set the terminal text color to green (color index 2):

`echotc AF 2`

- Move the cursor up one line:

`echotc up`
