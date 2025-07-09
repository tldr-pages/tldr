# last

> Vea los últimos usuarios conectados.
> Más información: <https://manned.org/last>.

- Vea la información del último inicio de sesión (por ejemplo, nombre de usuario, terminal, tiempo de arranque, kernel) de todos los usuarios leída de `/var/log/wtmp`:

`last`

- Lista la información de inicio de sesión de un usuario específico:

`last {{nombre_de_usuario}}`

- Especifica cuántos de los últimos inicios de sesión mostrar:

`last {{[-n|--limit]}} {{cuenta_inicios}}`

- Muestra la fecha y hora completas de las entradas y, a continuación, muestra la columna del nombre de host en último lugar para evitar que se trunque:

`last {{[-F|--fulltimes]}} {{[-a|--hostlast]}}`

- Visualiza todos los inicios de sesión de un usuario específico y muestra la dirección IP en lugar del nombre de host:

`last {{nombre_de_usuario}} {{[-i|--ip]}}`

- Lista la información desde una fecha y hora determinadas:

`last {{[-s|--since]}} {{-7days}}`

- Vea todos los reinicios registrados (es decir, los últimos inicios de sesión del pseudousuario "reboot"):

`last reboot`

- Muestra la ayuda:

`last {{[-h|--help]}}`
