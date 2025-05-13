# rofi

> Un lanzador de aplicaciones y conmutador de ventanas.
> Más información: <https://github.com/davatorium/rofi#manpage>.

- Muestra la lista de aplicaciones:

`rofi -show drun`

- Muestra la lista de todos los comandos:

`rofi -show run`

- Cambia entre ventanas:

`rofi -show window`

- Envía una lista de elementos a `stdin` y muestra el elemento seleccionado en `stdout`:

`printf "{{Opción1\nOpción2\nOpción3}}" | rofi -dmenu`
