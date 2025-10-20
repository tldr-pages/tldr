# systemctl freeze

> Congela una o más unidades.
> Las unidades congeladas se pueden reanudar con `systemctl thaw`.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#freeze%20PATTERN%E2%80%A6>.

- Congela una unidad específica:

`systemctl freeze {{unidad}}`

- Congela múltiples unidades:

`systemctl freeze {{unidad1 unidad2 ...}}`

- Congela todas las unidades en ejecución:

`systemctl freeze '*'`
