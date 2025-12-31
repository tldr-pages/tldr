# systemctl is-enabled

> Verifica si los archivos de unidad están habilitados.
> Vea también: `systemctl enable`, `systemctl disable`.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#is-enabled%20UNIT%E2%80%A6>.

- Muestra el estado de habilitación:

`systemctl is-enabled {{unidad1 unidad2 ...}}`

- Suprime la salida y devuelve solo el código de salida:

`systemctl is-enabled {{unidad}} --quiet`

- Muestra destinos de instalación y rutas de enlaces simbólicos:

`systemctl is-enabled {{unidad}} --full`
