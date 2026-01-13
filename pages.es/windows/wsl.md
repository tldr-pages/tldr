# wsl

> Administra el Subsistema de Windows para Linux.
> Más información: <https://learn.microsoft.com/windows/wsl/reference>.

- Iniciar un shell de Linux (usando la distribución predeterminada):

`wsl {{comando_de_shell}}`

- Ejecuta un comando de Linux sin usar un intérprete de comandos:

`wsl {{[-e|--exec]}} {{comando}} {{argumentos_del_comando}}`

- Especifica una distribución particular:

`wsl {{[-d|--distribution]}} {{distribución}} {{comando_de_shell}}`

- Lista las distribuciones disponibles:

`wsl {{[-l|--list]}}`

- Exporta una distribución a un archivo `.tar`:

`wsl --export {{distribución}} {{ruta\a\archivo_de_distribucion.tar}}`

- Importar una distribución de un archivo `.tar`:

`wsl --import {{distribución}} {{ruta\a\ubicacion_de_instalacion}} {{ruta\a\archivo_de_distribucion.tar}}`

- Cambiar la versión de wsl usada para la distribución especificada:

`wsl --set-version {{distribución}} {{versión}}`

- Apagar el Subsistema de Windows para Linux:

`wsl --shutdown`
