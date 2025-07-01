# ptyxis

> A container-oriented terminal for GNOME
> Ptyxis is a terminal for GNOME that focuses on ease-of-use in a world of containers.
> More information: <https://gitlab.gnome.org/chergert/ptyxis>.

- Open a new ptyxis window:

`ptyxis --new-window`

- Execute a specfic command in a new terminal window:

`ptyxis -x <command>`

- Open new tab ub the last opened window:

`ptyxis --tab`

- Set the title for a new:

`ptyxis --tab [-T|--title] <title>`

- Specify the working directory for a new tab, window, or command execution

`ptyxis [-d|--working-directory]=<DIR> --tab`
