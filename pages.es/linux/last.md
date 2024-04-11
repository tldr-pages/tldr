# last

> Lista la información de los últimos inicios de sesión de usuario.
> Vea también: `lastb`, `login`.
> Más información: <https://manned.org/last.1>.

- Lista la información de inicio de sesión (por ejemplo, nombre de usuario, terminal, tiempo de arranque, kernel) de todos los usuarios:

`last`

- Lista la información de inicio de sesión de un usuario específico:

`last {{nombredeusuario}}`

- Mostra la información de un TTY específico:

`last {{tty1}}`

- Lista la información actualizada (por defecto, la más reciente aparece al principio):

`last | tac`

- Muestra información sobre el arranque del sistema:

`last "{{system boot}}"`

- Lista información con un formato específico de marca de [t]iempo:

`last --time-format {{notime|full|iso}}`

- Lista información desde una fecha y hora específicas:

`last --since {{-7days}}`

- Muestra información (es decir, nombre de host e IP) de hosts remotos:

`last --dns`
