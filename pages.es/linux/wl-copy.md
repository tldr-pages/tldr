# wl-copy

> Limpia y copia al portapapeles de Wayland.
> Vea también: `wl-paste`, `xclip`.
> Más información: <https://github.com/bugaevc/wl-clipboard>.

- Copia el texto al portapapeles:

`wl-copy "{{texto}}"`

- Envía la salida del comando (`ls`) al portapapeles:

`{{ls}} | wl-copy`

- Copia solo para pegar una única vez y luego lo limpia:

`wl-copy --paste-once "{{texto}}"`

- Copia una imagen:

`wl-copy < {{ruta/a/la/imagen}}`

- Limpia el portapapeles:

`wl-copy --clear`
