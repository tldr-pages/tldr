# logger

> Añade mensajes al registro del sistema.
> Más información: <https://manned.org/logger>.

- Registra un mensaje en syslog:

`logger {{mensaje}}`

- Toma la entrada de `stdin` y la registra en syslog:

`echo {{entrada_de_registro}} | logger`

- Envía la salida a un servidor syslog remoto que se ejecuta en un puerto determinado. El puerto por defecto es 514:

`echo {{entrada_de_registro}} | logger {{[-n|--server]}} {{hostname}} {{[-P|--port]}} {{puerto}}`

- Utiliza una etiqueta específica para cada línea registrada. Por defecto es el nombre del usuario conectado:

`echo {{entrada_de_registro}} | logger {{[-t|--tag]}} {{etiqueta}}`

- Registra mensajes con una prioridad determinada. Por defecto es `user.notice`. Vea `man logger` para todas las opciones de prioridad:

`echo {{entrada_de_registro}} | logger {{[-p|--priority]}} {{user.warning}}`
