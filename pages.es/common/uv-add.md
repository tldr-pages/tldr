# uv add

> Añade dependencias de paquetes al archivo `pyproject.toml`.
> Los paquetes se especifican según <https://peps.python.org/pep-0508/>.
> Más información: <https://docs.astral.sh/uv/reference/cli/#uv-add>.

- Añade la última versión de un paquete:

`uv add {{paquete}}`

- Añade múltiples paquetes:

`uv add {{paquete1 paquete2 ...}}`

- Añade un paquete con un requisito de versión:

`uv add {{paquete>=1.2.3}}`

- Añade paquetes a un grupo de dependencia opcional, que se incluirá cuando se publique:

`uv add --optional {{opcional}} {{paquete1 paquete2 ...}}`

- Añade paquetes a un grupo local, que no se incluirán cuando se publiquen:

`uv add --group {{grupo}} {{paquete1 paquete2 ...}}`

- Añade paquetes al grupo dev, abreviatura de `--group dev`:

`uv add --dev {{paquete1 paquete2 ...}}`

- Añade paquete como editable:

`uv add --editable {{ruta/a/paquete/}}`

- Habilita un extra al instalar el paquete, se puede proporcionar varias veces:

`uv add {{paquete}} --extra {{característica_extra}}`
