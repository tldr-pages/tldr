# echotc

> Output termcap terminal capability codes in Zsh.
> Part of the `zsh/termcap` module.
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>.

- Load the termcap module before use:

`zmodload zsh/termcap`

- Return the cursor to the start of the current line (carriage return):

`echotc cr`

- Clear the screen:

`echotc cl`

- Set the terminal text color to green (color index 2):

`echotc AF 2`

- Move the cursor up one line:

`echotc up`
