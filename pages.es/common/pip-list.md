# pip list

> Lista los paquetes de Python instalados.
> Más información: <https://pip.pypa.io/en/stable/cli/pip_list/>.

- Lista los paquetes instalados:

`pip list`

- Lista los paquetes desactualizados que se pueden actualizar:

`pip list {{[-o|--outdated]}}`

- Lista los paquetes actualizados:

`pip list {{[-u|--uptodate]}}`

- Lista los paquetes en formato JSON:

`pip list --format json`

- Lista los paquetes que no son requeridos por otros paquetes:

`pip list --not-required`

- Lista los paquetes instalados solo en el directorio del usuario:

`pip list --user`

- Lista los paquetes y excluye los paquetes editables de la salida:

`pip list --exclude-editable`

- Lista los paquetes en formato freeze (a diferencia de `pip freeze`, no muestra información de instalaciones editables):

`pip list --format freeze`
