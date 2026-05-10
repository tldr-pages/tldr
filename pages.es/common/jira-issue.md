# jira issue

> Gestiona incidencias en un proyecto de Jira.
> Más información: <https://github.com/ankitpokhrel/jira-cli#issue>.

- Muestra las incidencias recientes:

`jira issue {{[ls|list]}}`

- Muestra una lista de incidencias asignadas a un usuario específico:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} "{{correo_electronico_o_mostrar_nombre}}"`

- Muestra una lista de incidencias de alta prioridad que me han sido asignadas:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Crea una incidencia mediante un indicador interactivo:

`jira issue create`

- Edita un problema mediante un indicador interactivo:

`jira issue edit`

- Asigna un usuario a un problema mediante un indicador interactivo:

`jira issue {{[asg|assign]}}`

- Mueve una incidencia a un estado determinado:

`jira issue {{[mv|move]}} {{id_incidencia}} "{{En progreso}}"`

- Abre una incidencia en el terminal utilizando `less`:

`jira issue view {{id_incidencia}}`
