# dtach

> Run a program in a session you can detach from and reattach to.
> See also: `screen`, `tmux`, `abduco`.
> More information: <https://manned.org/dtach>.

- Start a new session and attach to it:

`dtach -c {{path/to/socket}} {{bash}}`

- Start a new session without attaching to it:

`dtach -n {{path/to/socket}} {{bash}}`

- Attach to an existing session:

`dtach -a {{path/to/socket}}`

- Attach to a session, creating it if it does not exist:

`dtach -A {{path/to/socket}} {{bash}}`

- Detach from the current session:

`<Ctrl \>`

- Attach using the `winch` redraw method (useful for full-screen programs):

`dtach -a {{path/to/socket}} -r winch`
