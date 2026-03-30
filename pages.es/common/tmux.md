# tmux

> Multiplexor de terminal.
> Permite múltiples sesiones con ventanas, paneles y más.
> Ver también: `zellij`, `screen`.
> Más información: <https://github.com/tmux/tmux>.

- Inicia una nueva sesión:

`tmux`

- Inicia una nueva sesión con [n]ombre:

`tmux {{[new|new-session]}} -s {{nombre}}`

- Lista las sesiones existentes:

`tmux {{[ls|list-sessions]}}`

- Se adjunta a la sesión usada más recientemente:

`tmux {{[a|attach]}}`

- Se desconecta de la sesión actual (dentro de una sesión tmux):

`<Ctrl b><d>`

- Crea una nueva ventana (dentro de una sesión tmux):

`<Ctrl b><c>`

- Cambia entre sesiones y ventanas (dentro de una sesión tmux):

`<Ctrl b><w>`

- Termina una sesión por nombre de [o]bjetivo:

`tmux kill-session -t {{nombre}}`
