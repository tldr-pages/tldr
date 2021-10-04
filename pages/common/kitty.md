# kitty

> A fast, feature-rich, GPU based terminal emulator.
> More information: <https://sw.kovidgoyal.net/kitty/>.

- Open a new terminal:

`kitty`

- Open a terminal with the specified title for the window:

`kitty --title "{{title}}"`

- Start the theme-chooser builtin:

`kitty +kitten themes`

- Display an image in the terminal:

`kitty +kitten icat {{path/to/image}}`

- Copy the contents of stdin to the clipboard:

`echo {{example}} | kitty +kitten clipboard`
