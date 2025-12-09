# wofi

> Un lanzador de aplicaciones para compositores Wayland basados en wlroots, similar a `rofi` y `dmenu`.
> Más información: <https://manned.org/wofi>.

- Muestra la lista de aplicaciones:

`wofi {{[-S|--show]}} drun`

- Muestra la lista de todos los comandos:

`wofi {{[-S|--show]}} run`

- Envía una lista de elementos a `stdin` e imprime el elemento seleccionado en `stdout`:

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi {{[-d|--dmenu]}}`
