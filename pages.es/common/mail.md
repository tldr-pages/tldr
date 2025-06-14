# mail

> El comando opera en el buzón de correo del usuario si no se da ningún argumento.
> Para enviar un correo electrónico, el cuerpo del mensaje se construye desde `stdin`.
> Más información: <https://manned.org/mail>.

- Abre un prompt interactivo para revisar el correo personal:

`mail`

- Envía un mensaje de correo con CC opcional. La línea de comandos continúa después de presionar `<Intro>`. Ingresa el texto del mensaje (pueden ser varias líneas). Presiona `<Ctrl d>` para indicar el final del texto del mensaje:

`mail --subject "{{título del correo electrónico}}" {{para_usuario@example.com}} --cc "{{cc_correo_electrónico}}"`

- Envía un correo electrónico que contiene el contenido de un archivo:

`mail --subject "{{$HOSTNAME archivo.txt}}" {{para_usuario@example.com}} < {{ruta/al/archivo.txt}}`

- Envía un archivo `tar.gz` como adjunto:

`tar cvzf - {{ruta/al/directorio1 ruta/al/directorio2}} | uuencode {{data.tar.gz}} | mail --subject "{{asunto}}" {{a_usuario@example.com}}`

- Muestra la ayuda:

`mail {{[-h|--help]}}`
