# az config

> Administra la configuración de Azure CLI.
> Parte de `azure-cli`.
> Más información: <https://learn.microsoft.com/cli/azure/config>.

- Muestra todas las configuraciones:

`az config get`

- Muestra las configuraciones para una sección específica:

`az config get {{nombre_de_sección}}`

- Establece una configuración:

`az config set {{nombre_de_configuración}}={{valor}}`

- Elimina una configuración:

`az config unset {{nombre_de_configuración}}`
