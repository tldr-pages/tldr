# az group

> Administra grupos de recursos e implementaciones de plantillas.
> Parte de `azure-cli`.
> Más información: <https://docs.microsoft.com/cli/azure/group>.

- Crea un nuevo grupo de recursos:

`az group create --nombre {{nombre}} --ubicación {{ubicación}}`

- Comprueba si existe un grupo de recursos:

`az group exists --nombre {{nombre}}`

- Elimina un grupo de recursos:

`az group delete --nombre {{nombre}}`

- Coloca un grupo de recursos en estado de espera hasta que se cumpla una condición:

`az group wait --nombre {{nombre}} --{{created|deleted|exists|updated}}`
