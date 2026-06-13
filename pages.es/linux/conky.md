# conky

> Monitor de sistema ligero para X.
> Más información: <https://github.com/brndnmtthws/conky>.

- Ejecuta con la configuración por defecto:

`conky`

- Crea una nueva configuración por defecto:

`conky {{[-C|--print-config]}} > ~/.conkyrc`

- Ejecuta conky con un archivo de configuración concreto:

`conky {{[-c|--config]}} {{ruta/a/la/configuración}}`

- Ejecuta en segundo plano (daemon):

`conky {{[-d|--daemonize]}}`

- Alinea conky en el escritorio:

`conky {{[-a|--alignment]}} {{top|bottom|middle}}_{{left|right|middle}}`

- Pausa de 5 segundos al iniciar antes de ejecutarlo:

`conky {{[-p|--pause]}} {{5}}`
