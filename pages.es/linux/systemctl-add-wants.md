# systemctl add-wants

> Agrega dependencias `Wants` a un target para una o más unidades.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#add-wants%20TARGET%20UNIT%E2%80%A6>.

- Agrega una dependencia `Wants` desde un target a una unidad:

`systemctl add-wants {{target}} {{unidad}}`

- Agrega múltiples dependencias `Wants` a la vez:

`systemctl add-wants {{target}} {{unidad1 unidad2 ...}}`

- Agrega una dependencia `Wants` a nivel de usuario:

`systemctl add-wants {{target}} {{unidad}} --user`
