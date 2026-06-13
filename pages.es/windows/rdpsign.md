# rdpsign

> Una herramienta para firmar archivos del Protocolo de Escritorio Remoto (RDP).
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/rdpsign>.

- Firmar un archivo RDP:

`rdpsign {{ruta\al\archivo.rdp}}`

- Firmar un archivo RDP utilizando un hash sha256 específico:

`rdpsign {{ruta\al\archivo.rdp}} /sha265 {{hash}}`

- Habilitar salida silenciosa:

`rdpsign {{ruta\al\archivo.rdp}} /q`

- Mostrar advertencias, mensajes y estados detallados:

`rdpsign {{ruta\al\archivo.rdp}} /v`

- Probar la firma mostrando la salida en `stdout` sin actualizar el archivo:

`rdpsign {{ruta\al\archivo.rdp}} /l`
