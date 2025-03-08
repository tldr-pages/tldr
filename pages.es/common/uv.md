# uv

> Un rápido gestor de paquetes y proyectos Python.
> Algunos subcomandos como `tool` y `python` tienen su propia documentación de uso.
> Más información: <https://docs.astral.sh/uv/reference/cli>.

- Crea un nuevo proyecto Python en el directorio actual:

`uv init`

- Crear un nuevo proyecto Python en la ruta especificada:

`uv init {{ruta/a/directorio}}`

- Añade una nueva dependencia al proyecto:

`uv add {{paquete}}`

- Elimina una dependencia del proyecto:

`uv remove {{paquete}}`

- Ejecuta un script en el entorno del proyecto:

`uv run {{ruta/al/script.py}}`

- Ejecuta un comando en el entorno del proyecto:

`uv run {{comando}}`

- Actualiza el entorno de un proyecto desde `pyproject.toml`:

`uv sync`

- Crea un archivo de bloqueo para las dependencias del proyecto:

`uv lock`
