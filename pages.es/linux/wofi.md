# wofi

> Un lanzador de aplicaciones para compositores Wayland basados en wlroots, similar a `rofi` y `dmenu`.
> Más información: <https://hg.sr.ht/~scoopta/wofi>.

- Muestra la lista de aplicaciones:

`wofi --show drun`

- Muestra la lista de todos los comandos:

`wofi --show run`

- Envía una lista de elementos a `stdin` e imprime el elemento seleccionado en `stdout`:

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi --dmenu`
