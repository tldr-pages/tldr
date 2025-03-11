# ubus

> Interactúa con un servidor ubusd OpenWrt.
> Más información: <https://openwrt.org/docs/techref/ubus>.

- Lista los objetos disponibles:

`ubus list`

- Recupera información del sistema en formato JSON:

`ubus call system board`

- Escucha eventos:

`ubus subscribe {{nombre_evento}}`
