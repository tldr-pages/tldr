# tmux

> Multiplexa varias consolas virtuales.
> Más información: <https://github.com/tmux/tmux>.

- Inicia una nueva sesión de tmux:

`tmux`

- Inicia una nueva sesión de tmux y le asigna un nombre:

`tmux new -s {{nombre}}`

- Muestra las sesiones:

`tmux ls`

- Adjunta a una sesión:

`tmux a`

- Adjunta a una sesión con un nombre específico:

`tmux a -t {{nombre}}`

- Desconecta de la sesión:

`Ctrl + B, D`

- Elimina una sesión con un nombre específico:

`tmux kill-session -t {{nombre}}`

- Elimina una sesión cuando se adjunta:

`Ctrl + B, x (luego se pulsa 'y' para confirmar que sí)`
