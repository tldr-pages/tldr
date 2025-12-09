# wsl

> Administra el Subsistema de Windows para Linux.
> Más información: <https://learn.microsoft.com/windows/wsl/reference>.

- Iniciar un shell de Linux (usando la distribución predeterminada):

`wsl {{comando_de_shell}}`

- Ejecutar un comando de Linux sin usar un shell:

`wsl --exec {{comando}} {{argumentos_del_comando}}`

- Especificar una distribución particular:

`wsl --distribution {{distribución}} {{comando_de_shell}}`

- Listar las distribuciones disponibles:

`wsl --list`

- Exportar una distribución a un archivo `.tar`:

`wsl --export {{distribución}} {{ruta\a\archivo_de_distribucion.tar}}`

- Importar una distribución de un archivo `.tar`:

`wsl --import {{distribución}} {{ruta\a\ubicacion_de_instalacion}} {{ruta\a\archivo_de_distribucion.tar}}`

- Cambiar la versión de wsl usada para la distribución especificada:

`wsl --set-version {{distribución}} {{versión}}`

- Apagar el Subsistema de Windows para Linux:

`wsl --shutdown`
