# systemctl revert

> Restaura los archivos de unidad a sus versiones de origen.
> Deshace los efectos de `edit`, `enable`, `disable`, `set-property` y `mask`.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#revert%20UNIT%E2%80%A6>.

- Restaura los archivos de unidad a su configuración predeterminada:

`systemctl revert {{unidad1 unidad2 ...}}`

- Restaura un archivo de unidad de usuario:

`systemctl revert {{unidad}} --user`
