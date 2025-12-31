# sfc

> Escanea la integridad de los archivos del sistema de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- Muestra información sobre el uso del comando:

`sfc`

- Escanea todos los archivos del sistema y, si es posible, reparar cualquier problema:

`sfc /scannow`

- Escanea todos los archivos del sistema sin intentar reparar ninguno:

`sfc /verifyonly`

- Escanea un archivo específico y, si es posible, reparar cualquier problema:

`sfc /scanfile={{ruta\al\archivo}}`

- Escanea un archivo específico sin intentar repararlo:

`sfc /verifyfile={{ruta\al\archivo}}`

- Al reparar sin conexión, especificar el directorio de arranque:

`sfc /offbootdir={{ruta\al\directorio}}`

- Al reparar sin conexión, especificar el directorio de Windows:

`sfc /offwindir={{ruta\al\directorio}}`
