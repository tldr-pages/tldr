# poetry

> Gestiona paquetes y dependencias de Python.
> Algunos subcomandos, como `about`, `check`, `env`, etc., cuentan con su propia documentación de uso.
> Vea también: `asdf`, `pipenv`, `hatch`.
> Más información: <https://python-poetry.org/docs/cli/>.

- Crea un nuevo proyecto de Poetry en el directorio con un nombre específico:

`poetry new {{nombre_del_proyecto}}`

- Instala y añade una dependencia y sus subdependencias al archivo `pyproject.toml` del directorio actual:

`poetry add {{dependencia}}`

- Instala las dependencias del proyecto utilizando el archivo `pyproject.toml` del directorio actual:

`poetry install`

- Inicializa de forma interactiva (añade `-n` para hacerlo de forma no interactiva) el directorio actual como un nuevo proyecto de Poetry:

`poetry init`

- Descarga la última versión de todas las dependencias y actualiza `poetry.lock`:

`poetry update`

- Ejecuta un comando dentro del entorno virtual del proyecto:

`poetry run {{comando}}`

- Actualiza la versión del proyecto en `pyproject.toml`:

`poetry version {{patch|minor|major|prepatch|preminor|premajor|prerelease}}`

- Abre un intérprete de comandos dentro del entorno virtual del proyecto (para versiones anteriores a la 2.0, use `poetry shell`):

`eval «$(poetry env activate)»`
