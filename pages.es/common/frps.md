# frps

> Configura rápidamente un servicio de proxy inverso.
> Parte de `frp`.
> Más información: <https://github.com/fatedier/frp>.

- Inicia el servicio, utilizando el archivo de configuración por defecto (se supone que es `frps.ini` en el directorio actual):

`frps`

- Inicia el servicio, utilizando el nuevo archivo de configuración TOML (`frps.toml` en lugar de `frps.ini`) en el directorio actual:

`frps {{[-c|--config]}} ./frps.toml`

- Inicia el servicio, utilizando un archivo de configuración especificado:

`frps {{[-c|--config]}} {{ruta/al/archivo}}`

- Comprueba si el archivo de configuración es válido:

`frps verify {{[-c|--config]}} {{ruta/al/archivo}}`

- Imprime secuencia de comandos de configuración de autocompletado para Bash, fish, PowerShell o Zsh:

`frps completion {{bash|fish|powershell|zsh}}`

- Muestra versión:

`frps {{[-v|--version]}}`
