# uv tree

> Muestra las dependencias del proyecto en formato de árbol.
> Más información: <https://docs.astral.sh/uv/reference/cli/#uv-tree>.

- Muestra el árbol de dependencias del entorno actual:

`uv tree`

- Muestra el árbol de dependencias para todos los entornos:

`uv tree --universal`

- Muestra el árbol de dependencias hasta una determinada profundidad:

`uv tree {{[-d|--depth]}} {{n}}`

- Muestra la última versión disponible para todos los paquetes obsoletos:

`uv tree --outdated`

- Excluye dependencias del grupo dev:

`uv tree --no-dev`

- Muestra el árbol invertido, para que los hijos sean dependientes en lugar de dependencias:

`uv tree --invert`
