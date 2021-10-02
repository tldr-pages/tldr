# kitty

> A fast, feature-rich, GPU based terminal emulator.
> More information: <https://sw.kovidgoyal.net/kitty/>.

- Open the terminal with a title of `Example`:

`kitty --title {{Example}}`

- Start the theme-chooser builtin:

`kitty +kitten themes`

- Display `Example.jpg` in the terminal:

`kitty +kitten icat {{Example.jpg}}`

- Put `hooray` into the system clipboard:

`echo {{hooray}} | kitty +kitten clipboard`
