# az tag

> Administra etiquetas en un recurso de Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/tag>.

- Crea un valor de etiqueta:

`az tag add-value {{[-n|--name]}} {{nombre_de_etiqueta}} --value {{valor_de_etiqueta}}`

- Crea una etiqueta en la suscripción:

`az tag create {{[-n|--name]}} {{nombre_de_etiqueta}}`

- Elimina una etiqueta de la suscripción:

`az tag delete {{[-n|--name]}} {{nombre_de_etiqueta}}`

- Enumera todas las etiquetas de una suscripción:

`az tag list --resource-id /subscriptions/{{identificador_de_subscripción}}`

- Elimina un valor de etiqueta para un nombre de etiqueta específico:

`az tag remove-value {{[-n|--name]}} {{nombre_de_etiqueta}} --value {{valor_de_etiqueta}}`
