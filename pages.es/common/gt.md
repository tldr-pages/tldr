# gt

> Crea y gestiona secuencias de cambios de código dependientes (stacks) para Git y GitHub.
> Más información: <https://graphite.dev/docs/get-started>.

- Inicializa `gt` para el repositorio en el directorio actual:

`gt init`

- Crea una nueva rama apilada sobre la rama actual y confirmar los cambios por etapas:

`gt create {{nombre_de_rama}}`

- Crea un nuevo commit y arreglar las ramas apiladas:

`gt modify -cam {{mensaje_de_commit}}`

- Fuerza el push de todas las ramas de la pila actual a GitHub y crea o actualiza PRs:

`gt stack submit`

- Comprueba una rama diferente (solicita el modo interactivo cuando se omite el nombre de la rama):

`gt co {{nombre_rama}}`

- Sincroniza la pila con la versión remota (también elimina las ramas fusionadas):

`gt sync`

- Registra todas las pilas rastreadas:

`gt log short`

- Muestra la ayuda de un subcomando específico:

`gt {{subcomando}} --help`
