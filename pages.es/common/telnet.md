# telnet

> Se conecta a un puerto específico de un host mediante el protocolo telnet.
> Más información: <https://manned.org/telnet>.

- Se conecta mediante telnet al puerto predeterminado de un host:

`telnet {{host}}`

- Se conecta mediante Telnet a un puerto específico de un host:

`telnet {{dirección_ip}} {{puerto}}`

- [Interactivo] Sale de una sesión de Telnet:

`quit`

- Emite la combinación de caracteres de escape predeterminada para finalizar la sesión:

`<Ctrl ]>`

- Inicia `telnet` con "x" como carácter de finalización de sesión:

`telnet {{[-e|--escape]}} {{x}} {{dirección_ip}} {{puerto}}`

- Utiliza telnet para acceder a la animación de Star Wars:

`telnet {{towel.blinkenlights.nl}}`
