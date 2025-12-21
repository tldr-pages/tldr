# systemctl add-requires

> Agrega dependencias `Requires` a un target para una o más unidades.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#add-wants%20TARGET%20UNIT%E2%80%A6>.

- Agrega una dependencia `Requires` desde un target a una unidad:

`systemctl add-requires {{target}} {{unidad}}`

- Agrega múltiples dependencias `Requires` a la vez:

`systemctl add-requires {{target}} {{unidad1 unidad2 ...}}`

- Agrega una dependencia `Requires` a nivel de usuario:

`systemctl add-requires {{target}} {{unidad}} --user`
