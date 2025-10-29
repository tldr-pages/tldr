# az storage blob

> Administra contenedores y objetos de almacenamiento de blobs en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/storage/blob>.

- Descarga un blob a una ruta de acceso de archivo especificando un contenedor de origen:

`az storage blob download --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}} {{[-f|--file]}} {{ruta/al/archivo}}`

- Descarga blobs desde un contenedor de blobs recursivamente:

`az storage blob download-batch --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-s|--source]}} {{nombre_contenedor}} --pattern {{filename_regex}} {{[-d|--destination]}} {{ruta/al/destino}}`

- Sube un archivo local al almacenamiento de blobs:

`az storage blob upload --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}} {{[-f|--file]}} {{ruta/al/archivo}}`

- Elimina un objeto blob:

`az storage blob delete --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}}`

- Genera una firma de acceso compartido para un blob:

`az storage blob generate-sas --account-name {{nombre_cuenta_almacenamiento}} --account-key {{llave_cuenta_almacenamiento}} {{[-c|--container-name]}} {{nombre_contenedor}} {{[-n|--name]}} {{nombre_blob}} --permissions {{grupo_permisos}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
