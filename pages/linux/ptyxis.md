# ptyxis

> A container-oriented terminal for GNOME.
> More information: <https://gitlab.gnome.org/chergert/ptyxis#basic-usage--command-line-options>.

- Open a new Ptyxis window:

`ptyxis --new-window`

- Execute a specific command in a new terminal window:

`ptyxis {{[-x|--execute]}} {{command}}`

- Open new tab in the last opened window:

`ptyxis --tab`

- Set the title for a new:

`ptyxis --tab {{[-T|--title]}} {{title}}`

- Specify the working directory for a new tab, window, or command execution:

`ptyxis {{[-d|--working-directory]}} {{path/to/directory}} --tab`
