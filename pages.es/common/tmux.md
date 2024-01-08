# tmux

> Multiplexor de terminal.
> Permite múltiples sesiones con ventanas, paneles y más.
> Vea también: `zellij`, `screen`.
> Más información: <https://github.com/tmux/tmux>.

- Inicia una nueva sesión:

`tmux`

- Inicia una nueva sesión con nombre:

`tmux new -s {{nombre}}`

- Lista las sesiones existentes:

`tmux ls`

- Adjunta a la última sesión utilizada:

`tmux attach`

- Separa la sesión actual (dentro de una sesión tmux):

`<Ctrl>-B d`

- Crea una nueva ventana (dentro de una sesión tmux):

`<Ctrl>-B c`

- Cambia entre sesiones y ventanas (dentro de una sesión tmux):

`<Ctrl>-B w`

- Da de baja una sesión por su nombre:

`tmux kill-session -t {{nombre}}`
