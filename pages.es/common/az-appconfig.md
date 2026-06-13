# az appconfig

> Administra las configuraciones de aplicaciones en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/appconfig>.

- Crea una configuración de aplicación:

`az appconfig create {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-l|--location]}} {{ubicación}}`

- Elimina una configuración de aplicación específica:

`az appconfig delete {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_de_configuración}}`

- Lista todas las configuraciones de aplicaciones bajo la suscripción actual:

`az appconfig list`

- Lista todas las configuraciones de aplicaciones bajo un grupo de recursos específico:

`az appconfig list {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Muestra las propiedades de una configuración de aplicación:

`az appconfig show {{[-n|--name]}} {{nombre_de_configuración}}`

- Actualiza una configuración de aplicación específica:

`az appconfig update {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_de_configuración}}`
