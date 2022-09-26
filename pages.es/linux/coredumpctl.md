# coredumpctl

> Recupera y procesa volcados de memoria y sus metadatos.
> Más información: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Lista todos los volcados de memoria capturados:

`coredumpctl list`

- Lista los volcados de memoria capturados para un programa:

`coredumpctl list {{programa}}`

- Muestra información sobre los volcados de memoria que coincidan con el `PID` de un programa:

`coredumpctl info {{PID}}`

- Invoca el depurador usando el último volcado de memoria para un programa:

`coredumpctl debug {{programa}}`

- Extrae el último volcado de memoria a un fichero:

`coredumpctl --output={{ruta/al/archivo}} dump {{programa}}`
