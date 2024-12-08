# hatch

> Gestor de proyectos Python moderno y extensible.
> Vea también: `poetry`.
> Más información: <https://hatch.pypa.io/latest/cli/reference/>.

- Crea un nuevo proyecto Hatch:

`hatch new {{nombre_del_proyecto}}`

- Inicializa Hatch para un proyecto existente:

`hatch new --init`

- Construye un proyecto Hatch:

`hatch build`

- Elimina artefactos de construcción:

`hatch clean`

- Crea un entorno por defecto con las dependencias definidas en el archivo `pyproject.toml`:

`hatch env create`

- Muestra las dependencias del entorno en forma de tabla:

`hatch dep show table`
