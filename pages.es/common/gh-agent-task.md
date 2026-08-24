# gh agent-task

> Gestiona las tareas del agente de GitHub.
> Más información: <https://cli.github.com/manual/gh_agent-task>.

- Muestra las tareas del agente más recientes:

`gh {{[agent|agent-task]}} list`

- Crea una nueva tarea del agente para el repositorio actual:

`gh {{[agent|agent-task]}} create "{{Mejorar el rendimiento del proceso de procesamiento de datos}}"`

- Crea una nueva tarea de agente a partir de un archivo:

`gh {{[agent|agent-task]}} create {{[-F|--from-file]}} {{ruta/a/archivo}}`

- Muestra detalles sobre una tarea de agente específica:

`gh {{[agent|agent-task]}} view {{session_id|pr_number|url|branch}}`

- Muestra el registro de una tarea de agente específica:

`gh {{[agent|agent-task]}} view --log {{session_id|pr_number|url|branch}}`
