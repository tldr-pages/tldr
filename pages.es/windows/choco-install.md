# choco install

> Instalar uno o más paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-install>.

- Instalar uno o más paquetes:

`choco install {{paquete1 paquete2 ...}}`

- Instalar paquetes desde un archivo de configuración personalizado:

`choco install {{ruta\al\archivo_paquetes.config}}`

- Instalar un archivo `nuspec` o `nupkg` específico:

`choco install {{ruta\al\archivo}}`

- Instalar una versión específica de un paquete:

`choco install {{paquete}} --version {{versión}}`

- Permitir la instalación de múltiples versiones de un paquete:

`choco install {{paquete}} --allow-multiple`

- Confirmar automáticamente todos los mensajes:

`choco install {{paquete}} --yes`

- Especificar una fuente personalizada para recibir paquetes:

`choco install {{paquete}} --source {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco install {{paquete}} --user {{nombre_usuario}} --password {{contraseña}}`
