# systemctl try-restart

> Reinicia una o más unidades solo si están actualmente en ejecución.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#try-restart%20PATTERN%E2%80%A6>.

- Reinicia una unidad específica si está en ejecución:

`systemctl try-restart {{unidad}}`

- Reinicia varias unidades si están en ejecución:

`systemctl try-restart {{unidad1 unidad2 ...}}`

- Reinicia todas las unidades que coincidan con un patrón si están en ejecución:

`systemctl try-restart “{{patrón}}”`
