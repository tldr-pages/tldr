# choco install

> Instala uno o más paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-install>.

- Instala uno o más paquetes:

`choco install {{paquete1 paquete2 ...}}`

- Instala paquetes desde un archivo de configuración personalizado:

`choco install {{ruta\al\archivo_de_paquetes.config}}`

- Instala un archivo `nuspec` o `nupkg` específico:

`choco install {{path\to\file}}`

- Instala una versión específica de un paquete:

`choco install {{paquete}} --version {{versión}}`

- Permite instalar varias versiones de un paquete:

`choco install {{paquete}} --allow-multiple`

- Confirma todas las solicitudes automáticamente:

`choco install {{paquete}} --yes`

- Especifica una fuente personalizada desde la cual recibir los paquetes:

`choco install {{paquete}} --source {{url_fuente|alias}}`

- Proporciona un nombre de usuario y una contraseña para la autenticación:

`choco install {{paquete}} --user {{nombre_usuario}} --password {{contraseña}}`
