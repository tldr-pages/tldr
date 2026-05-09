# jira sprint

> Gestiona sprints en un tablero de proyecto de Jira.
> Más información: <https://github.com/ankitpokhrel/jira-cli#sprint>.

- Muestra una lista de sprints y sus incidencias en una vista de explorador:

`jira sprint {{[ls|list]}}`

- Muestra los problemas del sprint actual:

`jira sprint {{[ls|list]}} --current`

- Muestra los problemas del sprint actual que me han sido asignados:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Muestra los problemas de alta prioridad del sprint actual que me han sido asignados:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Añade problemas a un sprint mediante un indicador interactivo:

`jira sprint add`
