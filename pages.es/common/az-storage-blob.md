# az storage blob

> Administra contenedores y objetos de almacenamiento de blobs en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/storage/blob>.

- Descarga un blob a una ruta de acceso de archivo especificando un contenedor de origen:

`az storage blob download --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}} {{[-f|--file]}} {{ruta/al/archivo_local}}`

- Descargue blobs desde un contenedor de blobs recursivamente:

`az storage blob download-batch --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-s|--source]}} {{nombre_contenedor}} {{[-d|--destination]}} {{ruta/a/destino}} --pattern {{filename_regex}}`

- Upload a local file to blob storage:

`az storage blob upload --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}} {{[-f|--file]}} {{ruta/al/archivo_local}}`

- Delete a blob object:

`az storage blob delete --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}}`

- Generate a shared access signature for a blob:

`az storage blob generate-sas --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}} --permissions {{grupo_permisos}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
