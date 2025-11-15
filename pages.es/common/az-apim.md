# az apim

> Administra los servicios de Azure API Management.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/apim>.

- Enumera las instancias del servicio API Management:

`az apim list --resource-group {{grupo_de_recursos}}`

- Crea una instancia de servicio de API Management:

`az apim create --name {{nombre}} --resource-group {{grupo_de_recursos}} --publisher-email {{email}} --publisher-name {{name}}`

- Elimina una instancia del servicio de API Management:

`az apim delete --name {{nombre}} --resource-group {{grupo_de_recursos}}`

- Muestra detalles de una instancia del servicio de API Management:

`az apim show --name {{nombre}} --resource-group {{grupo_de_recursos}}`

- Actualiza una instancia del servicio API Management:

`az apim update --name {{nombre}} --resource-group {{grupo_de_recursos}}`
