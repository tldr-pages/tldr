# az storage container

> Administra contenedores de almacenamiento de blobs en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/storage/container>.

- Crea un contenedor en una cuenta de almacenamiento:

`az storage container create --account-name {{nombre_cuenta_almacenamiento}} {{[-n|--name]}} {{nombre_contenedor}} --public-access {{nivel_acceso}} --fail-on-exist`

- Genera una firma de acceso compartido para el contenedor:

`az storage container generate-sas --account-name {{nombre_cuenta_almacenamiento}} {{[-n|--name]}} {{nombre_contenedor}} --permissions {{permisos_sas}} --expiry {{fecha_caducidad}} --https-only`

- Lista los contenedores en una cuenta de almacenamiento:

`az storage container list --account-name {{nombre_cuenta_almacenamiento}} --prefix {{filtrar_prefijo}}`

- Marca el contenedor especificado para su eliminación:

`az storage container delete --account-name {{nombre_cuenta_almacenamiento}} {{[-n|--name]}} {{nombre_contenedor}} --fail-not-exist`
