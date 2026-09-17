# az group

> Administra grupos de recursos e implementaciones de plantillas.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/group>.

- Crea un nuevo grupo de recursos:

`az group create {{[-n|--name]}} {{nombre}} {{[-l|--location]}} {{ubicación}}`

- Comprueba si existe un grupo de recursos:

`az group exists {{[-n|--name]}} {{nombre}}`

- Elimina un grupo de recursos:

`az group delete {{[-n|--name]}} {{nombre}}`

- Coloca un grupo de recursos en estado de espera hasta que se cumpla una condición:

`az group wait {{[-n|--name]}} {{nombre}} --{{created|deleted|exists|updated}}`
