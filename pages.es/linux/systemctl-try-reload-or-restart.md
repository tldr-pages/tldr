# systemctl try-reload-or-restart

> Recarga una o más unidades si lo admiten; de lo contrario, las reinicia.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#try-reload-or-restart%20PATTERN%E2%80%A6>.

- Recarga o reinicia una unidad específica:

`systemctl try-reload-or-restart {{unidad}}`

- Recarga o reinicia varias unidades:

`systemctl try-reload-or-restart {{unidad1 unidad2 ...}}`

- Recarga o reinicia todas las unidades que coincidan con un patrón:

`systemctl try-reload-or-restart '{{patrón}}'`
