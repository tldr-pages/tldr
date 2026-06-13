# az apim

> Administra los servicios de Azure API Management.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/apim>.

- Enumera las instancias del servicio API Management:

`az apim list {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Crea una instancia de servicio de API Management:

`az apim create {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}} --publisher-email {{email}} --publisher-name {{name}}`

- Elimina una instancia del servicio de API Management:

`az apim delete {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Muestra detalles de una instancia del servicio de API Management:

`az apim show {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Actualiza una instancia del servicio API Management:

`az apim update {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`
