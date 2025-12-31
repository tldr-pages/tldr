# asterisk

> Ejecuta y administra instancias de servidores telefónicos e intercambiadores (teléfonos).
> Más información: <https://docs.asterisk.org/Operation/>.

- [R]econecta a un servidor en ejecución y activa el registro con 3 niveles de [v]erbosidad:

`asterisk -r -vvv`

- [R]econecta a un servidor en ejecución, ejecuta un solo comando y regresa:

`asterisk -r -x "{{comando}}"`

- Muestra los clientes chan_SIP (teléfonos):

`asterisk -r -x "sip show peers"`

- Muestra las llamadas y canales activos:

`asterisk -r -x "core show channels"`

- Muestra los buzones de voz:

`asterisk -r -x "voicemail show users"`

- Termina un canal:

`asterisk -r -x "hangup request {{ID_del_canal}}"`

- Recarga la configuración de chan_SIP:

`asterisk -r -x "sip reload"`
