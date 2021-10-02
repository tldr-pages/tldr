# kitty

> A fast, feature-rich, GPU based terminal emulator.
> More information: <https://sw.kovidgoyal.net/kitty/>.

- Open a terminal with the specified title for the window:

`kitty --title "{{title}}"`

- Start the theme-chooser builtin:

`kitty +kitten themes`

- Display an image in the terminal:

`kitty +kitten icat {{path/to/image.jpg}}`

- Put `hooray` into the system clipboard:

`echo {{hooray}} | kitty +kitten clipboard`
