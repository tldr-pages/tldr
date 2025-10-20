# systemctl is-active

> Verifica si una o más unidades de systemd están activas.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#is-active%20PATTERN%E2%80%A6>.

- Verifica si una unidad está activa:

`systemctl is-active {{unidad}}`

- Verifica si múltiples unidades están activas:

`systemctl is-active {{unidad1 unidad2 ...}}`

- Verifica si una unidad está activa sin imprimir el estado en `stdout`:

`systemctl is-active {{unidad}} {{[-q|--quiet]}}`

- Verifica si una unidad de usuario está activa:

`systemctl is-active {{unidad}} --user`
