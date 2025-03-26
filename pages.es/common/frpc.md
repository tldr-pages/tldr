# frpc

> Conéctate a un servidor `frps` para iniciar conexiones proxy en el host actual.
> Parte de `frp`.
> Más información: <https://github.com/fatedier/frp>.

- Inicia el servicio, utilizando el archivo de configuración por defecto (se supone que es `frps.ini` en el directorio actual):

`frpc`

- Inicia el servicio, utilizando el nuevo archivo de configuración TOML (`frps.toml` en lugar de `frps.ini`) en el directorio actual:

`frpc {{[-c|--config]}} ./frps.toml`

- Inicia el servicio, utilizando un archivo de configuración específico:

`frpc {{[-c|--config]}} {{ruta/al/archivo}}`

- Comprueba si el archivo de configuración es válido:

`frpc verify {{[-c|--config]}} {{ruta/al/archivo}}`

- Imprime secuencia de comandos de configuración de autocompletado para Bash, fish, PowerShell o Zsh:

`frpc completion {{bash|fish|powershell|zsh}}`

- Muestra versión:

`frpc {{[-v|--version]}}`
