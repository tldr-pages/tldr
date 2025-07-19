# certutil

> Una herramienta para gestionar y configurar información de certificados.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- Exporta la información de configuración o archivos:

`certutil {{nombre_de_archivo}}`

- Encripta un archivo en hexadecimal:

`certutil -encodehex {{ruta\al\archivo_entrada}} {{ruta\al\archivo_salida}}`

- Encripta un archivo a Base64:

`certutil -encode {{ruta\al\archivo_entrada}} {{ruta\al\archivo_salida}}`

- Decodifica un archivo codificado en Base64:

`certutil -decode {{ruta\al\archivo_entrada}} {{ruta\al\archivo_salida}}`

- Genera y muestra un hash criptográfico sobre un archivo:

`certutil -hashfile {{ruta\al\archivo_entrada}} {{md2|md4|md5|sha1|sha256|sha384|sha512}}`
