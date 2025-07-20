# msg

> Enviar un mensaje a un usuario o sesión.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- Envía un mensaje a un usuario o sesión especificada:

`msg {{nombre_de_usuario|nombre_de_sesión|id_de_sesión}} {{mensaje}}`

- Envía un mensaje desde `stdin`:

`echo "{{mensaje}}" | msg {{nombre_de_usuario|nombre_de_sesión|id_de_sesión}}`

- Envía un mensaje a un servidor específico:

`msg /server:{{nombre_del_servidor}} {{nombre_de_usuario|nombre_de_sesión|id_de_sesión}}`

- Envía un mensaje a todos los usuarios de la máquina actual:

`msg *`

- Establece un retraso en segundos para un mensaje:

`msg /time:{{10}}`
