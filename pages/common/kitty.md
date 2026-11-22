# kitty

> A fast, feature-rich, GPU based terminal emulator.
> More information: <https://sw.kovidgoyal.net/kitty/>.

- Open a new terminal:

`kitty`

- Run a command in a new terminal window:

`kitty {{command}}`

- Open a terminal with a fixed operating system window title:

`kitty {{[-T|--title]}} "{{title}}"`

- Open a terminal using the built-in defaults:

`kitty {{[-c|--config]}} NONE`

- Choose and apply a color theme interactively (updates `kitty.conf`):

`kitty +kitten themes`

- Display an image in a terminal that supports the kitty graphics protocol:

`kitty +kitten icat "{{path/to/image}}"`

- Copy text to the clipboard (requires a terminal that allows OSC 52 writes):

`printf '%s' "{{text}}" | kitty +kitten clipboard`
