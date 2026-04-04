# az storage

> Administra los recursos de Azure Cloud Storage.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/storage>.

- Crea una cuenta de almacenamiento:

`az storage account create {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_de_cuenta}} {{[-l|--location]}} {{ubicación}} --sku {{account_sku}}`

- Enumera todas las cuentas de almacenamiento de un grupo de recursos:

`az storage account list {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Enumera las claves de acceso de una cuenta de almacenamiento:

`az storage account keys list {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_de_cuenta}}`

- Elimina una cuenta de almacenamiento:

`az storage account delete {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_de_cuenta}}`

- Actualiza la versión mínima de TLS para una cuenta de almacenamiento:

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_de_cuenta}}`
