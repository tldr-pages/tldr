# az appconfig

> Administra las configuraciones de aplicaciones en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/appconfig>.

- Crea una configuración de aplicación:

`az appconfig create --name {{nombre}} --resource-group {{grupo_de_recursos}} --location {{ubicación}}`

- Elimina una configuración de aplicación específica:

`az appconfig delete --resource-group {{grupo_de_recursos}} --name {{nombre_de_configuración}}`

- Lista todas las configuraciones de aplicaciones bajo la suscripción actual:

`az appconfig list`

- Lista todas las configuraciones de aplicaciones bajo un grupo de recursos específico:

`az appconfig list --resource-group {{grupo_de_recursos}}`

- Muestra las propiedades de una configuración de aplicación:

`az appconfig show --name {{nombre_de_configuración}}`

- Actualiza una configuración de aplicación específica:

`az appconfig update --resource-group {{grupo_de_recursos}} --name {{nombre_de_configuración}}`
