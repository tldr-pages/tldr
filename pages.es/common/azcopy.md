# azcopy

> Copia datos desde y hacia Azure Storage.
> Vea también: `az storage`.
> Más información: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10#list-of-commands>.

- Inicia sesión en un inquilino de Azure:

`azcopy login`

- Carga un archivo local:

`azcopy {{[c|copy]}} '{{ruta/al/archivo_origen}}' 'https://{{nombre_cuenta_almacenamiento}}.blob.core.windows.net/{{nombre_contenedor}}/{{nombre_blob}}'`

- Carga archivos con extensiones `.txt` y `.jpg`:

`azcopy {{[c|copy]}} '{{ruta/al/directorio_origen}}' 'https://{{nombre_cuenta_almacenamiento}}.blob.core.windows.net/{{nombre_contenedor}}' --include-pattern '*.txt;*.jpg'`

- Copia un contenedor directamente entre dos cuentas de almacenamiento de Azure:

`azcopy {{[c|copy]}} 'https://{{nombre_cuenta_almacenamiento_origen}}.blob.core.windows.net/{{nombre_contenedor}}' 'https://{{nombre_cuenta_almacenamiento_destino}}.blob.core.windows.net/{{nombre_contenedor}}'`

- Sincroniza un directorio local y elimina archivos en el destino si ya no existen en el origen:

`azcopy {{[s|sync]}} '{{ruta/al/directorio_origen}}' 'https://{{nombre_cuenta_almacenamiento}}.blob.core.windows.net/{{nombre_contenedor}}' --delete-destination true`

- Muestra la ayuda:

`azcopy {{[-h|--help]}}`
