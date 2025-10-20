# az storage account

> Administra cuentas de almacenamiento en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/storage/account>.

- Crea una cuenta de almacenamiento:

`az storage account create {{[-n|--name]}} {{nombre_cuenta_almacenamiento}} {{[-g|--resource-group]}} {{grupo_recurso_azure}} --location {{ubicación_azure}} --sku {{cuenta_almacenamiento_sku}}`

- Genera una firma de acceso compartido para una cuenta de almacenamiento específica:

`az storage account generate-sas --account-name {{nombre_cuenta_almacenamiento}} {{[-n|--name]}} {{nombre_cuenta}} --permissions {{permisos_sas}} --expiry {{fecha_caducidad}} --services {{servicios_almacenamiento}} --resource-types {{tipos_recursos}}`

- Lista cuentas de almacenamiento:

`az storage account list {{[-g|--resource-group]}} {{grupo_recurso_azure}}`

- Elimina una cuenta de almacenamiento específica:

`az storage account delete {{[-n|--name]}} {{nombre_cuenta_almacenamiento}} {{[-g|--resource-group]}} {{grupo_recurso_azure}}`
