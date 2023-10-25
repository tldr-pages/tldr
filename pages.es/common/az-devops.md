# az devops

> Administra organizaciones de Azure DevOps.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/devops?view=azure-cli-latest>.

- Configura el Token de Acceso Personal (PAT) para iniciar sesión en una organización específica:

`az devops login --organization {{url_de_la_organización}}`

- Abre un proyecto en el navegador:

`az devops project show --project {{nombre_de_proyecto}} --open`

- Lista los miembros de un equipo específico que trabaja en un proyecto en particular:

`az devops team list-member --project {{nombre_de_proyecto}} --team {{nombre_de_equipo}}`

- Comprueba la configuración actual de la CLI de Azure DevOps:

`az devops configure --list`

- Configura el comportamiento de la CLI de Azure DevOps estableciendo un proyecto predeterminado y una organización predeterminada:

`az devops configure --defaults project={{nombre_de_proyecto}} organization={{url_de_la_organización}}`
