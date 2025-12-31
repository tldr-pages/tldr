# xfreerdp

> Implementación del protocolo del Free Remote Desktop.
> Más información: <https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface-(possibly-not-up-to-date,-check-application-help-text-for-most-up-to-date-version)>.

- Conéctate a un servidor FreeRDP:

`xfreerdp /u:{{usuario}} /p:{{contraseña}} /v:{{dirección_ip}}`

- Conéctate a un servidor FreeRDP y activa la redirección de la salida de audio mediante el dispositivo `sys:alsa`:

`xfreerdp /u:{{usuario}} /p:{{contraseña}} /v:{{dirección_ip}} /sound:{{sys:alsa}}`

- Conéctate a un servidor FreeRDP con resolución dinámica:

`xfreerdp /v:{{dirección_ip}} /u:{{usuario}} /p:{{contraseña}} /dynamic-resolution`

- Conéctate a un servidor FreeRDP con redirección del portapapeles:

`xfreerdp /v:{{dirección_ip}} /u:{{usuario}} /p:{{contraseña}} +clipboard`

- Conéctate a un servidor FreeRDP ignorando cualquier comprobación de certificado:

`xfreerdp /v:{{dirección_ip}} /u:{{usuario}} /p:{{contraseña}} /cert:ignore`

- Conéctate a un servidor FreeRDP con un directorio compartido:

`xfreerdp /v:{{dirección_ip}} /u:{{usuario}} /p:{{contraseña}} /drive:{{ruta/al/directorio}},{{nombre_compartido}}`
