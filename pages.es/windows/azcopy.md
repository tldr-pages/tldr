# azcopy

> Una herramienta de transferencia de archivos para subir a cuentas de almacenamiento en la nube de Azure.
> Más información: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- Inicia sesión en un inquilino de Azure:

`azcopy login`

- Sube un archivo local:

`azcopy copy '{{ruta\al\archivo_origen}}' 'https://{{nombre_cuenta_almacenamiento}}.blob.core.windows.net/{{nombre_contenedor}}/{{nombre_blob}}'`

- Sube archivos con extensiones `.txt` y `.jpg`:

`azcopy copy '{{ruta\al\directorio_origen}}' 'https://{{nombre_cuenta_almacenamiento}}.blob.core.windows.net/{{nombre_contenedor}}' --include-pattern '{{*.txt;*.jpg}}'`

- Copia un contenedor directamente entre dos cuentas de almacenamiento de Azure:

`azcopy copy 'https://{{nombre_cuenta_almacenamiento_origen}}.blob.core.windows.net/{{nombre_contenedor}}' 'https://{{nombre_cuenta_almacenamiento_destino}}.blob.core.windows.net/{{nombre_contenedor}}'`

- Sincroniza un directorio local y elimina archivos en el destino si ya no existen en el origen:

`azcopy sync '{{ruta\al\directorio_origen}}' 'https://{{nombre_cuenta_almacenamiento}}.blob.core.windows.net/{{nombre_contenedor}}' --recursive --delete-destination=true`

- Muestra ayuda:

`azcopy --help`
