# obsidian

> Interfaz de línea de comandos para la aplicación de toma de notas Obsidian Markdown.
> Nota: Requiere que la aplicación Obsidian esté en ejecución.
> Más información: <https://obsidian.md/help/cli>.

- Abre la nota diaria de hoy:

`obsidian daily`

- Añade una tarea a la nota diaria del día actual:

`obsidian daily:append content="- [ ] {{tarea}}"`

- Crea una nueva nota a partir de una plantilla:

`obsidian create name="{{nombre_nota}}" template={{nombre_nota}}`

- Busca texto en el banco de notas:

`obsidian search query="{{consulta_búsqueda}}"`

- Muestra todas las tareas pendientes del banco de notas:

`obsidian tasks todo`

- Lee una nota concreta:

`obsidian read file={{nombre_nota}}`

- Lee una nota en una ruta concreta relativa a la raíz del banco de notas:

`obsidian read path={{ruta/a/nota.md}}`

- Lee la nota activa:

`obsidian read`
