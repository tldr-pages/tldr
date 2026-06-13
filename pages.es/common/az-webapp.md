# az webapp

> Administra aplicaciones web alojadas en Azure Cloud Services.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/webapp>.

- Lista los entornos de ejecución disponibles para una aplicación web:

`az webapp list-runtimes {{[-os|--os-type]}} {{windows|linux}}`

- Crea una aplicación web:

`az webapp up {{[-n|--name]}} {{nombre}} {{[-l|--location]}} {{ubicación}} {{[-r|--runtime]}} {{entorno_de_ejecución}}`

- Lista todas las aplicaciones web:

`az webapp list`

- Elimina una aplicación web específica:

`az webapp delete {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`
