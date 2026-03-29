# az devops

> Administra organizaciones de Azure DevOps.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/devops>.

- Configura el Token de Acceso Personal (PAT) para iniciar sesión en una organización específica:

`az devops login {{[--org|--organization]}} {{url_de_la_organización}}`

- Abre un proyecto en el navegador:

`az devops project show {{[-p|--project]}} {{nombre_de_proyecto}} --open`

- Lista los miembros de un equipo específico que trabaja en un proyecto en particular:

`az devops team list-member {{[-p|--project]}} {{nombre_de_proyecto}} --team {{nombre_de_equipo}}`

- Comprueba la configuración actual de la CLI de Azure DevOps:

`az devops configure {{[-l|--list]}}`

- Configura el comportamiento de la CLI de Azure DevOps estableciendo un proyecto predeterminado y una organización predeterminada:

`az devops configure {{[-d|--defaults]}} project={{nombre_de_proyecto}} organization={{url_de_la_organización}}`
